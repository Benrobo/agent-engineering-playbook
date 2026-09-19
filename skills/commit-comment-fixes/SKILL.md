---
name: commit-comment-fixes
description: "Package already implemented PR-comment fixes into traceable commits and optional requested replies."
---

# Commit Comment Fixes

Read the repository's active instruction files and inspect the relevant code, scripts, and canonical examples before acting. Follow the project's existing conventions and the current task. This procedure does not expand authorization.

## Workflow

1. Inspect staged and unstaged changes and the existing thread-to-fix mapping. Confirm which fixes belong in the requested commits; preserve unrelated hunks.
2. Group changes by coherent review concern where practical, without forcing broken intermediate commits. Stage only intended hunks and follow the repository commit convention.
3. Commit or push only within the user's requested scope. Do not reset, rebase, force-push, or rewrite history merely to clean up the presentation.
4. If replies are requested after a push, verify that the remote head contains the fixes. Link the canonical commit and relevant validation for each stable thread ID. A local commit hash is not evidence that a remote reviewer can see it.
5. Report commits, remote verification, and unresolved threads. Leave threads unresolved unless resolving them is also authorized.
