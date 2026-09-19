# investigate-errors

Investigate application error evidence and distinguish product failures from telemetry noise using scoped read-only correlation.

## Requirements

Error event or identifier, source code, and optional read-only observability access. No provider credentials belong in this folder. Configure connectors or CLIs through your coding agent's normal setup. If an integration is unavailable, use supplied evidence or return a local draft with the limitation stated.

## Set up with your coding agent

1. Copy this complete folder into `.agents/skills/investigate-errors/` for Codex, or `.claude/skills/investigate-errors/` for Claude Code. Compare and merge if a folder already exists.
2. Let the coding agent inspect this project's own instructions, manifests, examples, and commands before following the skill.
3. Invoke `$investigate-errors` in Codex or `/investigate-errors` in Claude Code. For other agents, consult their skill support; when unavailable, attach both Markdown files and explicitly ask the agent to follow them for the task.
4. Keep project-wide policy in your existing project instruction file. Add a short pointer to this skill when useful instead of copying its entire procedure there.

Official setup references: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills).

## Adapt to your project

Configure: **event tool; project/environment; time zone/window; release mapping; redaction rules; business invariants**. Replace framework or workflow choices only when your repository supports the replacement. Preserve the procedure's evidence requirements and scope boundaries. Remove steps that truly do not apply rather than inventing infrastructure to satisfy them.

Ask your agent: “Inspect this repository and the installed skill before using it. Follow the project's existing conventions and cite the files that establish them. Do not install tools or perform external actions.”

## Trial request

> Investigate this error event and tell me whether it represents a user-visible failure.

Expected behavior: Classification has traceable evidence, no hidden production writes, and uncertainty is explicit.

Try this on an isolated branch or synthetic evidence first. Check actual artifacts and tool results, not just the agent's summary. If it fails, change the narrow instruction responsible and rerun the same scenario. Structural validity alone does not prove behavioral quality.
