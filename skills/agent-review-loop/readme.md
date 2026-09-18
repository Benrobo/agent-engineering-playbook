# agent-review-loop

Run bounded review and fix rounds for a requested change. Use when repeated review is explicitly requested or justified; do not launch agents without permitted delegation.

## Requirements

Defined diff, review criteria, validation commands, and optionally an authorized independent reviewer. No provider credentials belong in this folder. Configure connectors or CLIs through your coding agent's normal setup. If an integration is unavailable, use supplied evidence or return a local draft with the limitation stated.

## Set up with your coding agent

1. Copy this complete folder into `.agents/skills/agent-review-loop/` for Codex, or `.claude/skills/agent-review-loop/` for Claude Code. Compare and merge if a folder already exists.
2. Populate `project-context.md` using verified project facts. Keep `SKILL.md` and that file together.
3. Invoke `$agent-review-loop` in Codex or `/agent-review-loop` in Claude Code. For other agents, consult their skill support; when unavailable, attach both Markdown files and explicitly ask the agent to follow them for the task.
4. Keep project-wide policy in your existing project instruction file. Add a short pointer to this skill when useful instead of copying its entire procedure there.

Official setup references: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills).

## Adapt to your project

Configure: **base revision; maximum rounds; reviewer tool availability; severity threshold; accepted findings log**. Replace framework or workflow choices only when your repository supports the replacement. Preserve the procedure's evidence requirements and scope boundaries. Remove steps that truly do not apply rather than inventing infrastructure to satisfy them.

Ask your agent: “Inspect my repository and propose project-specific edits to this skill and its context worksheet. Cite the files that establish each command and convention. Do not run deployments or modify external systems.” Review that proposed adaptation before adopting it.

## Trial request

> Run up to two review/fix rounds on this change; use sequential review if independent agents are unavailable.

Expected behavior: Bounded rounds, final revision evidence, and honest independence status; no endless retry or unrequested publication.

Try this on an isolated branch or synthetic evidence first. Check actual artifacts and tool results, not just the agent's summary. If it fails, change the narrow instruction responsible and rerun the same scenario. Structural validity alone does not prove behavioral quality.
