# investigate-integration

Trace a provider event through local persistence and business rules to diagnose missing or inconsistent integration state.

## Requirements

Provider/event identifiers, explicit environment, relevant state model, and read-only evidence access. No provider credentials belong in this folder. Configure connectors or CLIs through your coding agent's normal setup. If an integration is unavailable, use supplied evidence or return a local draft with the limitation stated.

## Set up with your coding agent

1. Copy this complete folder into `.agents/skills/investigate-integration/` for Codex, or `.claude/skills/investigate-integration/` for Claude Code. Compare and merge if a folder already exists.
2. Populate `project-context.md` using verified project facts. Keep `SKILL.md` and that file together.
3. Invoke `$investigate-integration` in Codex or `/investigate-integration` in Claude Code. For other agents, consult their skill support; when unavailable, attach both Markdown files and explicitly ask the agent to follow them for the task.
4. Keep project-wide policy in your existing project instruction file. Add a short pointer to this skill when useful instead of copying its entire procedure there.

Official setup references: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills).

## Adapt to your project

Configure: **provider; event types; id mapping; eligibility rules; webhook verification; retry semantics; local status machine**. Replace framework or workflow choices only when your repository supports the replacement. Preserve the procedure's evidence requirements and scope boundaries. Remove steps that truly do not apply rather than inventing infrastructure to satisfy them.

Ask your agent: “Inspect my repository and propose project-specific edits to this skill and its context worksheet. Cite the files that establish each command and convention. Do not run deployments or modify external systems.” Review that proposed adaptation before adopting it.

## Trial request

> Investigate why this provider event did not create the expected local record. Do not replay it.

Expected behavior: Provider truth, local state, and eligibility are checked before a cause is claimed; no replay occurs.

Try this on an isolated branch or synthetic evidence first. Check actual artifacts and tool results, not just the agent's summary. If it fails, change the narrow instruction responsible and rerun the same scenario. Structural validity alone does not prove behavioral quality.
