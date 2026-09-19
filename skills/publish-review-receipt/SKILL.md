---
name: publish-review-receipt
description: "Record a review receipt tied to an exact revision. Use when a user asks to publish or preserve review evidence; this is not a human approval."
---

# Publish Review Receipt

Read the repository's active instruction files and inspect the relevant code, scripts, and canonical examples before acting. Follow the project's existing conventions and the current task. This procedure does not expand authorization.

## Workflow

1. Collect the reviewed head and base, review scope, checks, findings, and accepted exceptions. Use the actual reviewer/model identity when known, otherwise say unknown.
2. Verify the remote revision before publishing remote evidence. If the head changed, re-review the changed scope or clearly mark the receipt stale; never attach old evidence as a current clean result.
3. Distinguish automated review from human approval. Record blocked checks and accepted findings with their real reason and decision source.
4. If publication is requested, update a matching existing receipt instead of creating duplicates. Use the exact requested destination and link the reviewed revision.
5. If external publication is unavailable or unauthorized, save a local receipt and state that nothing was posted. Report the receipt URL or local path and its limitations.
