# browser-ui-validation

Exercise a web flow and inspect its rendered result with the available browser.

## Requirements

A reachable app and a supported browser tool or existing browser tests. In-app browser access is preferred when available; no global CLI installation is required.

## Install and use

From the playbook root:

```sh
python3 install.py browser-ui-validation --project "/absolute/path/to/your-project" --agent both
```

Copy the complete folder when installing manually. Keep existing local edits;
use the installer's backup behavior for deliberate replacement. Normal automatic
skill selection remains enabled where supported. You can also request
`$browser-ui-validation` in Codex or `/browser-ui-validation` in Claude Code. This repository update does
not install the skill globally or into unrelated projects.

## Adaptation

Let the agent inspect the target repository and actual tools. Choose applicable
parts of the workflow from the task and evidence; do not create infrastructure
to satisfy an example. Keep project-specific policy in the project's instructions.

## Trial scenarios

> Verify the edited settings form in the current in-app tab, including failed save and retry.

Expected: Preserves the selected session, observes controls before interacting, verifies saved state and failure recovery, and reports real evidence.

> The app streams updates continuously and browser authentication is unavailable.

Expected: Waits for relevant UI state instead of universal network-idle; reports blocked authenticated checks without inventing success.

These are evaluation scenarios, not claims of executed integration tests. Check
actual artifacts and observations. Frontmatter validation only proves packaging.
