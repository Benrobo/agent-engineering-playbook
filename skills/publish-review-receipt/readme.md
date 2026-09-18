# publish-review-receipt

Record a review receipt tied to an exact revision. Use when a user asks to publish or preserve review evidence; this is not a human approval.

## Requirements

Completed review evidence, exact revision, and publication access only when requested. No provider credentials belong in this folder. Configure connectors or CLIs through your coding agent's normal setup. If an integration is unavailable, use supplied evidence or return a local draft with the limitation stated.

## Set up with your coding agent

1. Copy this complete folder into `.agents/skills/publish-review-receipt/` for Codex, or `.claude/skills/publish-review-receipt/` for Claude Code. Compare and merge if a folder already exists.
2. Populate `project-context.md` using verified project facts. Keep `SKILL.md` and that file together.
3. Invoke `$publish-review-receipt` in Codex or `/publish-review-receipt` in Claude Code. For other agents, consult their skill support; when unavailable, attach both Markdown files and explicitly ask the agent to follow them for the task.
4. Keep project-wide policy in your existing project instruction file. Add a short pointer to this skill when useful instead of copying its entire procedure there.

Official setup references: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills).

## Adapt to your project

Configure: **receipt destination; existing receipt identity; revision lookup; reviewer identity; evidence format**. Replace framework or workflow choices only when your repository supports the replacement. Preserve the procedure's evidence requirements and scope boundaries. Remove steps that truly do not apply rather than inventing infrastructure to satisfy them.

Ask your agent: “Inspect my repository and propose project-specific edits to this skill and its context worksheet. Cite the files that establish each command and convention. Do not run deployments or modify external systems.” Review that proposed adaptation before adopting it.

## Trial request

> Save a local review receipt for this revision with the actual checks and remaining findings.

Expected behavior: The receipt records head/base and limitations; it does not imply an approval or a published check.

Try this on an isolated branch or synthetic evidence first. Check actual artifacts and tool results, not just the agent's summary. If it fails, change the narrow instruction responsible and rerun the same scenario. Structural validity alone does not prove behavioral quality.
