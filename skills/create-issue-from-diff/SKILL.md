---
name: create-issue-from-diff
description: "Draft an issue from the actual behavior in a diff; create it in a tracker only when requested."
---

# Create Issue From Diff

Read the repository's active instruction files and inspect the relevant code, scripts, and canonical examples before acting. Scale the workflow to the task and evidence; use the project's actual tools and conventions. Existing user authorization remains valid, and this procedure does not expand it.

## Workflow

1. Read the diff and relevant surrounding behavior. Explain the user problem and intended outcome rather than listing file names.
2. Separate completed implementation facts from proposed follow-up work. Describe observed before/after behavior and link supporting evidence when available; do not infer user impact solely from a symbol name. Include concise acceptance criteria that can be verified without reading the conversation.
3. Search for an existing matching issue when tracker access exists. Reuse or reference it instead of creating duplicates.
4. Draft locally when creation is not requested or the tool is unavailable. If creation is authorized, use the verified project/team destination and report the returned URL/key.
5. Do not invent issue IDs, rename branches, edit PR metadata, or create additional tasks automatically. Flag uncertainty that changes the problem statement.
