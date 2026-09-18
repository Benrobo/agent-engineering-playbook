---
name: review-changes
description: "Review a defined diff for actionable behavioral defects with concrete evidence. Use for code review requests, not automatic stylistic rewriting."
---

# Review Changes

Read [project-context.md](project-context.md) for configured facts. Verify stale or missing facts against the repository; do not interpret unconfigured fields as values or permission. Follow the active task and project instructions. This procedure does not expand authorization.

## Workflow

1. Establish the requested diff and base. Prefer the explicit base, then the actual PR base; discover the repository default if needed rather than assuming a branch name. Include working changes only when in scope.
2. Read the issue intent and trace changed paths into callers, data models, and tests. Prioritize correctness, authorization, data integrity, concurrency, and regressions over personal style preferences.
3. Report only actionable findings tied to a concrete trigger and outcome. Include severity, precise file/line, why it fails, and a minimal fix direction. Distinguish hypotheses from established defects.
4. Consider unnecessary complexity and dead code when they cause a material problem. Respect intentionally accepted findings unless new facts alter their impact.
5. State coverage limits and the reviewed revision. No findings is not proof of correctness. Do not fix, approve, comment externally, or publish unless the user requested those actions.
