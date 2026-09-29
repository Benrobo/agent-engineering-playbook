---
name: debug-root-cause
description: "Diagnose reproducible bugs, failed tests, build failures, and intermittent behavior by testing competing explanations. Use when the cause is uncertain; preserve the distinction between investigation, mitigation, and a verified fix."
---

# Debug root cause

Establish expected and actual behavior, the affected version and environment,
and the smallest available reproduction. Read the full relevant error and
trace its path through the owning code. A recent change is a lead, not proof.

Choose the observation that best separates plausible causes. Compare a failing
case with a nearby working case, inspect a boundary, or add temporary scoped
instrumentation. Change one causal variable at a time when practical. Keep
facts, hypotheses, and missing evidence distinct; do not stack speculative
patches merely because each seems plausible.

For timing or integration failures, examine order, shared state, cancellation,
retries, and partial completion as indicated by evidence. Preserve the failure
signal while reducing a reproduction. Use isolated fixtures and existing test
facilities rather than replaying live side effects or disabling protections.

Once a cause is supported, fix the owning behavior within the requested scope.
Add a regression test when it usefully distinguishes the defect from correct
behavior. Verify the original failure path and a nearby valid case. A mitigation
can be appropriate when it reduces immediate impact; label it and retain the
unresolved cause instead of presenting it as a permanent fix.

If an experiment provides no new information, reconsider the hypothesis or
missing environment evidence before trying again. Stop an unproductive loop
with a concrete blocker and the smallest next observation needed. Report the
cause, evidence, correction or mitigation, and remaining uncertainty. Remove
temporary diagnostics that are no longer useful.

Research source: [systematic-debugging](https://www.skills.sh/obra/superpowers/systematic-debugging).
This adaptation retains hypothesis-driven investigation without imposing a
fixed number of phases, attempts, or mandatory tests for trivial changes.
