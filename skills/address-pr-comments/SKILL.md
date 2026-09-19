---
name: address-pr-comments
description: "Read unresolved review threads, triage requests, and implement scoped local fixes. Use when asked to address PR feedback."
---

# Address Pr Comments

Read the repository's active instruction files and inspect the relevant code, scripts, and canonical examples before acting. Follow the project's existing conventions and the current task. This procedure does not expand authorization.

## Workflow

1. Fetch complete unresolved threads, including context and stable comment/thread IDs. Exclude resolved threads and non-actionable acknowledgements unless requested.
2. Match each request to the current code. Classify it as a valid scoped fix, already addressed, needing explanation, or requiring a product/design decision.
3. Implement straightforward relevant fixes locally. Preserve unrelated edits and avoid expanding scope based solely on reviewer suggestions.
4. Validate changed behavior and retain a mapping from thread ID to files, evidence, and remaining decisions. If feedback conflicts, resolve against the task intent or ask for the actual missing decision.
5. Return a per-thread disposition. Do not send replies, resolve threads, push, or claim the reviewer has approved unless those actions are requested and supported.
