---
name: agent-review-loop
description: "Run bounded review and fix rounds for a requested change. Use when repeated review is explicitly requested or justified; do not launch agents without permitted delegation."
---

# Agent Review Loop

Read [project-context.md](project-context.md) for configured facts. Verify stale or missing facts against the repository; do not interpret unconfigured fields as values or permission. Follow the active task and project instructions. This procedure does not expand authorization.

## Workflow

1. Fix the review scope and record the initial revision and validation state. Default to at most three rounds unless the user sets another reasonable limit.
2. If delegation is available and authorized, give a fresh reviewer the actual diff and necessary context without seeding a preferred conclusion. Keep the implementer responsible for edits. Otherwise review sequentially and label the lack of independent review.
3. Triage findings by concrete impact. Implement scoped fixes and run relevant checks; record accepted findings with the user's reasons, not invented waivers.
4. Review the updated diff after material fixes. A review of an earlier revision cannot clear later changes. Reuse prior evidence only if the relevant diff and base are unchanged.
5. Stop on a clean final pass, round limit, or recurring blocker with no useful next step. Return revision, rounds, checks, unresolved findings, and limitations. Do not turn review completion into permission to commit, publish, or merge.
