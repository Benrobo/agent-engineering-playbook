# codebase-architecture

Choose owners and dependency boundaries from repository evidence, with readable
execution, project-aware formatting, and useful contract and decision comments.

## Requirements

Repository source, instructions, and relevant dependency/build configuration; no required language or framework.

## Install and use

From the playbook root:

```sh
python3 install.py codebase-architecture --project "/absolute/path/to/your-project" --agent both
```

Copy the complete folder when installing manually. Keep existing local edits;
use the installer's backup behavior for deliberate replacement. Normal automatic
skill selection remains enabled where supported. You can also request
`$codebase-architecture` in Codex or `/codebase-architecture` in Claude Code. This repository update does
not install the skill globally or into unrelated projects.

## Adaptation

Let the agent inspect the target repository and actual tools. Choose applicable
parts of the workflow from the task and evidence; do not create infrastructure
to satisfy an example. Keep project-specific policy in the project's instructions.

## Trial scenarios

> Add export generation to a small command-line project using its existing structure.

Expected: Keeps the command and domain behavior at appropriate existing boundaries; does not introduce web modules, classes, or a monorepo tree.

> Extract a helper used by two domains with different policies.

Expected: Checks whether the behavior has the same reason to change; sharing is not forced by similar syntax.

> Refactor an asynchronous operation with dense expressions and an undocumented
> ordering constraint, following this project's language and formatter.

Expected: Makes meaningful steps readable, preserves error and cleanup behavior,
documents the actual ordering constraint near its owner, and avoids comments
that merely repeat the code or impose another language's syntax.

These are evaluation scenarios, not claims of executed integration tests. Check
actual artifacts and observations. Frontmatter validation only proves packaging.
