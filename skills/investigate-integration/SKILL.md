---
name: investigate-integration
description: "Trace a provider event through local persistence and business rules to diagnose missing or inconsistent integration state."
---

# Investigate Integration

Read the repository's active instruction files and inspect the relevant code, scripts, and canonical examples before acting. Scale the workflow to the task and evidence; use the project's actual tools and conventions. Existing user authorization remains valid, and this procedure does not expand it.

## Workflow

1. Identify the exact provider event, account, timestamp, and local identifier mapping. Retrieve minimum necessary provider and database evidence without exposing credentials or personal payloads.
2. Trace the expected state machine from event receipt through validation, eligibility, mappings, persistence, and user visibility. Check feature flags and required fields before declaring a missing record a bug.
3. Compare provider truth with durable local state and relevant logs. Separate event time from arrival and processing time; inspect idempotency boundaries and transaction completion when deliveries are duplicated or out of order. Distinguish delivery failure, duplicate delivery, rejected eligibility, processing failure, and delayed projection.
4. Build a timeline and state what remains unknown. Propose a synthetic reproduction and regression test for the suspected failure path.
5. Keep the investigation read-only. Replays, retries, payouts, emails, record repairs, and state changes require a separately authorized action with concrete scope.
