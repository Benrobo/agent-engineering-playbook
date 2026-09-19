---
name: write-tests
description: "Write behavior-focused regression tests at the narrowest useful public boundary. Use when adding coverage for a change or reproducing a bug."
---

# Write Tests

Read the repository's active instruction files and inspect the relevant code, scripts, and canonical examples before acting. Follow the project's existing conventions and the current task. This procedure does not expand authorization.

## Workflow

1. Identify the failure or acceptance criterion the test must distinguish. Choose the smallest public boundary that still exercises the important behavior.
2. Keep deterministic domain logic real. Mock external services, time, randomness, or transport only where isolation needs them. Do not mock away the behavior under test.
3. Build minimal realistic fixtures that satisfy actual invariants. For database tests, use the configured isolated environment and clean up reliably; never select a production database by default.
4. Assert observable results, state transitions, and relevant errors rather than implementation call order. Do not export private helpers solely to test them.
5. For a bug fix, establish failing-then-passing evidence when feasible. Restore mocks and timers, run the targeted test, and record what coverage does not prove. Avoid adding tests that simply duplicate trivial implementation.
