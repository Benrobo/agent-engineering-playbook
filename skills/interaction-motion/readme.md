# interaction-motion

Make state transitions understandable, responsive, and consistent.

## Requirements

The existing UI runtime and motion implementation; browser/native inspection when available. No mandatory library or animation values.

## Install and use

From the playbook root:

```sh
python3 install.py interaction-motion --project "/absolute/path/to/your-project" --agent both
```

Copy the complete folder when installing manually. Keep existing local edits;
use the installer's backup behavior for deliberate replacement. Normal automatic
skill selection remains enabled where supported. You can also request
`$interaction-motion` in Codex or `/interaction-motion` in Claude Code. This repository update does
not install the skill globally or into unrelated projects.

## Adaptation

Let the agent inspect the target repository and actual tools. Choose applicable
parts of the workflow from the task and evidence; do not create infrastructure
to satisfy an example. Keep project-specific policy in the project's instructions.

## Trial scenarios

> Fix this drawer snapping when I close it halfway through opening.

Expected: Traces the state transition and cleanup, preserves existing tokens, verifies reversal and repeated input, and checks reduced motion.

> Polish a frequently used control in a product with no motion library.

Expected: Considers whether static feedback is enough and uses existing capabilities without installing a library for style alone.

These are evaluation scenarios, not claims of executed integration tests. Check
actual artifacts and observations. Frontmatter validation only proves packaging.
