# debug-root-cause

Use discriminating experiments to diagnose uncertain failures.

## Requirements

A failing case or credible diagnostic evidence and access to relevant source; isolated test tools where available.

## Install and use

From the playbook root:

```sh
python3 install.py debug-root-cause --project "/absolute/path/to/your-project" --agent both
```

Copy the complete folder when installing manually. Keep existing local edits;
use the installer's backup behavior for deliberate replacement. Normal automatic
skill selection remains enabled where supported. You can also request
`$debug-root-cause` in Codex or `/debug-root-cause` in Claude Code. This repository update does
not install the skill globally or into unrelated projects.

## Adaptation

Let the agent inspect the target repository and actual tools. Choose applicable
parts of the workflow from the task and evidence; do not create infrastructure
to satisfy an example. Keep project-specific policy in the project's instructions.

## Trial scenarios

> Find why a test fails only after another test has run.

Expected: Compares isolated and ordered execution, identifies shared state, and verifies the correction without hiding the failure behind retries.

> An external dependency is unavailable, so the original error cannot be reproduced.

Expected: Separates supported facts from hypotheses and proposes the smallest useful next observation.

These are evaluation scenarios, not claims of executed integration tests. Check
actual artifacts and observations. Frontmatter validation only proves packaging.
