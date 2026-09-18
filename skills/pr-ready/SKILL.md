---
name: pr-ready
description: "Prepare a change for review with scoped validation, current review evidence, and a clear PR description."
---

# Pr Ready

Read [project-context.md](project-context.md) for configured facts. Verify stale or missing facts against the repository; do not interpret unconfigured fields as values or permission. Follow the active task and project instructions. This procedure does not expand authorization.

## Workflow

1. Record branch, base, working changes, and existing PR state. Identify unrelated local work before staging anything.
2. Confirm the final diff matches the task. Run appropriate checks and review the current revision, reusing evidence only when the relevant diff and base are unchanged.
3. Draft the PR around the resulting behavior, why it matters, validation, and material limitations. Follow the repository template and keep the title aligned with the final scope.
4. Commit, push, or create/update a PR only when included in the user's authorization. Prefer a draft for incomplete checks if publication is requested and the limitation is explicit. Do not automatically rebase, force-push, or merge.
5. Return the reviewable result with its exact revision and check status. A polished description must not conceal failing or unexecuted validation.
