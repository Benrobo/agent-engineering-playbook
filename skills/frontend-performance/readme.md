# frontend-performance

Find and improve a measured frontend bottleneck.

## Requirements

A representative scenario and available profiling or existing performance reports; no required framework or profiling package.

## Install and use

From the playbook root:

```sh
python3 install.py frontend-performance --project "/absolute/path/to/your-project" --agent both
```

Copy the complete folder when installing manually. Keep existing local edits;
use the installer's backup behavior for deliberate replacement. Normal automatic
skill selection remains enabled where supported. You can also request
`$frontend-performance` in Codex or `/frontend-performance` in Claude Code. This repository update does
not install the skill globally or into unrelated projects.

## Adaptation

Let the agent inspect the target repository and actual tools. Choose applicable
parts of the workflow from the task and evidence; do not create infrastructure
to satisfy an example. Keep project-specific policy in the project's instructions.

## Trial scenarios

> Find why the search screen freezes while typing with a realistic large result set.

Expected: Measures the interaction, identifies the dominant cost, makes a justified change, and compares under the same conditions.

> Recommend improvements when no browser profiling is available.

Expected: Reports source-level hypotheses and a measurement plan, with no fabricated metrics or proven-gain claims.

These are evaluation scenarios, not claims of executed integration tests. Check
actual artifacts and observations. Frontmatter validation only proves packaging.
