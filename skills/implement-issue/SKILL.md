---
name: implement-issue
description: "Implement a scoped issue from its acceptance criteria and repository context. Use when a ticket or concrete bug is assigned for implementation."
---

# Implement Issue

Read the repository's active instruction files and inspect the relevant code, scripts, and canonical examples before acting. Follow the project's existing conventions and the current task. This procedure does not expand authorization.

## Workflow

1. Read the exact issue, attachments, and linked diagnostic evidence relevant to the request. Distinguish acceptance criteria from suggestions in comments. If the tracker is unavailable, use supplied text and identify missing context.
2. Trace the affected behavior through entry points, shared packages, persistence, and consumers. Establish reproduction or expected behavior before planning a fix.
3. For a nontrivial change, state the smallest implementation plan and observable success criteria. Follow the project's actual frontend/API conventions; do not introduce a competing framework.
4. Implement within scope, preserving unrelated changes. Add regression coverage where it distinguishes the failure from correct behavior.
5. Run the relevant available checks. Report changed behavior, evidence, and unresolved acceptance criteria. Do not create a branch, commit, publish, or start a review loop merely because this skill was loaded.
