---
name: generate-test-plan
description: "Convert a code diff into an executable manual test plan for affected user and system flows."
---

# Generate Test Plan

Read [project-context.md](project-context.md) for configured facts. Verify stale or missing facts against the repository; do not interpret unconfigured fields as values or permission. Follow the active task and project instructions. This procedure does not expand authorization.

## Workflow

1. Trace changed code to user-facing routes and background or API workflows. Include indirect callers affected by shared components or contracts.
2. Describe real prerequisites: account role, required records, feature flags, environment, and service availability. A page URL alone is not a reproducible setup.
3. Write ordered actions with observable expected results. Cover the primary behavior, meaningful errors, and a nearby regression path; do not enumerate irrelevant permutations.
4. Include non-UI checks for jobs, webhooks, persistence, or CLI behavior where the diff requires them. Use synthetic fixtures and avoid real payments, emails, or production mutations.
5. Label each case as planned, executed, passed, failed, or blocked with evidence. Do not describe a generated test plan as completed testing.
