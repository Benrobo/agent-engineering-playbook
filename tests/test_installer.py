import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='skill project ')
        self.project = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def run_install(self, *extra):
        return subprocess.run([sys.executable, str(ROOT/'install.py'), 'interface-craft', '--project', str(self.project), *extra], capture_output=True, text=True)

    def test_both_complete_and_idempotent(self):
        first = self.run_install('--agent', 'both')
        self.assertEqual(first.returncode, 0, first.stderr)
        for folder in ('.agents', '.claude'):
            target = self.project/folder/'skills/interface-craft'
            for source in (ROOT/'skills/interface-craft').rglob('*'):
                if source.is_file():
                    self.assertEqual(source.read_bytes(), (target/source.relative_to(ROOT/'skills/interface-craft')).read_bytes())
        second = self.run_install('--agent', 'both')
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertIn('Already installed', second.stdout)

    def test_dry_run_writes_nothing(self):
        result = self.run_install('--dry-run')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_local_edits_preserved_then_backed_up(self):
        self.assertEqual(self.run_install().returncode, 0)
        target = self.project/'.agents/skills/interface-craft/SKILL.md'
        target.write_text('My customized local skill')
        blocked = self.run_install()
        self.assertNotEqual(blocked.returncode, 0)
        self.assertEqual(target.read_text(), 'My customized local skill')
        replaced = self.run_install('--replace')
        self.assertEqual(replaced.returncode, 0, replaced.stderr)
        backups = list((self.project/'.agents/skill-backups').glob('*/SKILL.md'))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), 'My customized local skill')

    def test_install_does_not_add_project_files(self):
        result = self.run_install()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual({p.name for p in self.project.iterdir()}, {'.agents'})

    def test_conflict_preflight_prevents_partial_both_install(self):
        target = self.project/'.claude/skills/interface-craft'
        target.mkdir(parents=True)
        (target/'custom.txt').write_text('preserve')
        result = self.run_install('--agent', 'both')
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.project/'.agents').exists())
        self.assertEqual((target/'custom.txt').read_text(), 'preserve')

    def test_invalid_skill_cannot_escape_source(self):
        result = subprocess.run([sys.executable,str(ROOT/'install.py'),'../escape','--project',str(self.project)],capture_output=True,text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_refuse_destination_symlink(self):
        target = self.project/'.agents/skills/interface-craft'
        target.parent.mkdir(parents=True)
        elsewhere = self.project/'elsewhere'
        elsewhere.mkdir()
        target.symlink_to(elsewhere, target_is_directory=True)
        result = self.run_install('--replace')
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(target.is_symlink())
        self.assertEqual(list(elsewhere.iterdir()), [])

if __name__ == '__main__':
    unittest.main()
