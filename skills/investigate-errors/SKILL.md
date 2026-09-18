---
name: investigate-errors
description: "Investigate application error evidence and distinguish product failures from telemetry noise using scoped read-only correlation."
---

# Investigate Errors

Read [project-context.md](project-context.md) for configured facts. Verify stale or missing facts against the repository; do not interpret unconfigured fields as values or permission. Follow the active task and project instructions. This procedure does not expand authorization.

## Workflow

1. Establish the exact event, environment, time window, release, and affected operation. Retrieve only the evidence needed to investigate.
2. Trace first-party stack frames and correlate relevant requests or records with read-only access. Separate observed facts from hypotheses and missing evidence.
3. Classify the event as an application failure, expected condition captured incorrectly, third-party noise, or unresolved. Absence of repeated events does not prove harmlessness.
4. If proposing a capture filter, keep true nearby failures observable and describe a regression test. Prefer fixing the real product failure over silencing telemetry.
5. Report likely cause, impact, evidence, and a bounded next step. Do not replay events, retry jobs, repair data, or expose personal payloads as part of an investigation.
