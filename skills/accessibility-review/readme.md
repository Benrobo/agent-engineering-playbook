# accessibility-review

Find task barriers through semantics, keyboard behavior, and rendered checks.

## Requirements

Relevant source and, when available, browser/native and assistive-technology facilities. Automated tooling is optional and cannot prove conformance.

## Install and use

From the playbook root:

```sh
python3 install.py accessibility-review --project "/absolute/path/to/your-project" --agent both
```

Copy the complete folder when installing manually. Keep existing local edits;
use the installer's backup behavior for deliberate replacement. Normal automatic
skill selection remains enabled where supported. You can also request
`$accessibility-review` in Codex or `/accessibility-review` in Claude Code. This repository update does
not install the skill globally or into unrelated projects.

## Adaptation

Let the agent inspect the target repository and actual tools. Choose applicable
parts of the workflow from the task and evidence; do not create infrastructure
to satisfy an example. Keep project-specific policy in the project's instructions.

## Trial scenarios

> Check keyboard use of this dialog and fix the focus loss when it closes.

Expected: Traces the owning control, reproduces the sequence, fixes within existing primitives, and verifies focus restoration.

> Audit a native settings screen when only a web preview is available.

Expected: Uses source evidence where useful and clearly leaves native behavior unverified.

These are evaluation scenarios, not claims of executed integration tests. Check
actual artifacts and observations. Frontmatter validation only proves packaging.
