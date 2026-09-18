---
name: audit-slow-queries
description: "Audit measured SQL workload and connect expensive queries to application paths without changing production state."
---

# Audit Slow Queries

Read [project-context.md](project-context.md) for configured facts. Verify stale or missing facts against the repository; do not interpret unconfigured fields as values or permission. Follow the active task and project instructions. This procedure does not expand authorization.

## Workflow

1. Confirm the database and observation window. Use an existing read-only statistics source; do not default to production or request broad credentials.
2. Rank normalized queries by total cost as well as per-call latency, calls, and waits. Distinguish cumulative load from isolated slow execution and separate maintenance noise.
3. Trace high-impact query shapes to code, indexes, cardinality, and calling frequency. Explain the evidence for each suspected bottleneck.
4. Prefer existing plans or non-executing EXPLAIN where appropriate. EXPLAIN ANALYZE executes a query; use it only in an authorized safe environment with bounded cost and side effects understood.
5. Recommend query/index/application changes with expected benefit, tradeoffs, and a measurement plan. Do not execute schema changes, rewrite data, or run unbounded live queries during the audit.
