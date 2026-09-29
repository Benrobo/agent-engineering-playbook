---
name: validate-changes
description: "Select and run checks based on affected packages and actual CI configuration. Use to validate an implementation or prepare a handoff."
---

# Validate Changes

Read the repository's active instruction files and inspect the relevant code, scripts, and canonical examples before acting. Scale the workflow to the task and evidence; use the project's actual tools and conventions. Existing user authorization remains valid, and this procedure does not expand it.

## Workflow

1. Inspect the diff, project instructions, package scripts, and relevant CI jobs. Identify changed packages and consumers affected by public interfaces.
2. Choose the smallest useful set of checks, including required formatting. Use repository-supported task filters; do not invent a command or assume a monorepo tool.
3. Run checks against the final change and record exact commands and results. For changed UI behavior, exercise the relevant flow in an available browser or native runtime; prefer the in-app browser for web work unless another browser was selected. Static checks do not establish rendered correctness. Combine compatible scoped checks where useful. A command that did not execute is not a pass.
4. Separate introduced failures from demonstrated pre-existing failures and missing environment dependencies. Do not rewrite unrelated code to make a broad check green.
5. Broaden testing only when failures, changed behavior, or uncertainty justify it. Return a short validation record with revision/diff scope, passes, failures, and blocked checks.
