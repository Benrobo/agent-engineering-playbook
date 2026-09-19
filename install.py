#!/usr/bin/env python3
"""Install selected local playbook skills into an agent's discovery directory."""
import argparse
import hashlib
import re
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def manifest(folder):
    result = {}
    for path in sorted(folder.rglob('*')):
        if path.is_symlink():
            raise ValueError('Symlinks are not supported in skill packages: ' + str(path))
        if path.is_file():
            result[str(path.relative_to(folder))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def validate(folder, name):
    text = (folder / 'SKILL.md').read_text(encoding='utf-8')
    parts = text.split('---', 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError('Missing SKILL.md frontmatter: ' + name)
    if not re.search(r'^name:\s*' + re.escape(name) + r'\s*$', parts[1], re.M):
        raise ValueError('Skill name must match folder: ' + name)
    if not re.search(r'^description:\s*\S.+$', parts[1], re.M):
        raise ValueError('Missing one-line description: ' + name)
    for required in ('readme.md', 'project-context.md'):
        if not (folder / required).is_file():
            raise ValueError('Missing ' + required + ': ' + name)
    return manifest(folder)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skills', nargs='*', help='Skill folder names; installs only these skills')
    parser.add_argument('--list', action='store_true', help='List available skills')
    parser.add_argument('--agent', choices=['codex', 'claude', 'both'], default='codex')
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument('--project', type=Path, help='Existing project directory')
    scope.add_argument('--user', action='store_true', help='Install for this user across local projects')
    parser.add_argument('--dry-run', action='store_true', help='Validate and print destinations without writing')
    parser.add_argument('--replace', action='store_true', help='Back up and replace a different existing installation')
    args = parser.parse_args()
    if args.list:
        print('\n'.join(sorted(p.name for p in (ROOT / 'skills').iterdir() if (p / 'SKILL.md').is_file())))
        return 0
    if not args.skills or not (args.project or args.user):
        parser.error('choose skill names and either --project PATH or --user')
    base = args.project.expanduser().resolve() if args.project else Path.home()
    if not base.is_dir():
        parser.error('project directory must already exist: ' + str(base))
    agents = ['codex', 'claude'] if args.agent == 'both' else [args.agent]
    plans = []
    for name in dict.fromkeys(args.skills):
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
            parser.error('invalid skill name: ' + name)
        source = ROOT / 'skills' / name
        if not source.is_dir() or source.is_symlink():
            parser.error('unknown or unsupported skill: ' + name)
        expected = validate(source, name)
        for agent in agents:
            parent = base / ('.agents' if agent == 'codex' else '.claude') / 'skills'
            target = parent / name
            if target.is_symlink():
                raise ValueError('Refusing to replace symlink: ' + str(target))
            if source.resolve() == target.resolve():
                raise ValueError('Source is already the install destination')
            same = target.is_dir() and manifest(target) == expected
            if target.exists() and not same and not args.replace:
                raise ValueError('Existing installation differs: ' + str(target) + '\nReview it, then use --replace to back it up and replace it.')
            plans.append((source, target, expected, same, agent))
    for source, target, expected, same, agent in plans:
        if same:
            print('Already installed and verified: ' + str(target))
            continue
        if args.dry_run:
            print('Would install: ' + str(target))
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        backup = None
        with tempfile.TemporaryDirectory(prefix='.skill-install-', dir=target.parent) as temp:
            staged = Path(temp) / source.name
            shutil.copytree(source, staged)
            if manifest(staged) != expected:
                raise ValueError('Copy verification failed: ' + source.name)
            if target.exists():
                # Keep backups outside discovery folders so they cannot load as duplicate skills.
                backup_root = target.parent.parent / 'skill-backups'
                backup_root.mkdir(parents=True, exist_ok=True)
                stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
                backup = backup_root / (source.name + '-' + stamp)
                target.rename(backup)
            try:
                staged.rename(target)
            except Exception:
                if backup is not None and not target.exists():
                    backup.rename(target)
                raise
        if manifest(target) != expected:
            raise ValueError('Installed file verification failed: ' + str(target))
        print('Installed and verified: ' + str(target))
        if backup:
            print('Previous copy preserved: ' + str(backup))
        print('Invoke: ' + ('$' if agent == 'codex' else '/') + source.name)
    if not args.dry_run:
        print('Files are installed in agent discovery paths. If absent from the skill picker, restart the agent and check workspace trust/settings. Runtime activation is not verified by this installer.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError) as exc:
        print('Install failed: ' + str(exc), file=sys.stderr)
        sys.exit(1)
