# frontend-conventions

Apply existing UI, component, and form conventions while implementing frontend changes. Use for UI behavior and component work, not a wholesale redesign.

## Requirements

Frontend source, design-system examples, and a way to inspect the resulting UI. No provider credentials belong in this folder. Configure connectors or CLIs through your coding agent's normal setup. If an integration is unavailable, use supplied evidence or return a local draft with the limitation stated.

## Set up with your coding agent

1. Copy this complete folder into `.agents/skills/frontend-conventions/` for Codex, or `.claude/skills/frontend-conventions/` for Claude Code. Compare and merge if a folder already exists.
2. Populate `project-context.md` using verified project facts. Keep `SKILL.md` and that file together.
3. Invoke `$frontend-conventions` in Codex or `/frontend-conventions` in Claude Code. For other agents, consult their skill support; when unavailable, attach both Markdown files and explicitly ask the agent to follow them for the task.
4. Keep project-wide policy in your existing project instruction file. Add a short pointer to this skill when useful instead of copying its entire procedure there.

Official setup references: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills).

## Adapt to your project

Configure: **component library; canonical screens; form library; state/data fetching conventions; accessibility checks; legacy boundaries**. Replace framework or workflow choices only when your repository supports the replacement. Preserve the procedure's evidence requirements and scope boundaries. Remove steps that truly do not apply rather than inventing infrastructure to satisfy them.

Ask your agent: “Inspect my repository and propose project-specific edits to this skill and its context worksheet. Cite the files that establish each command and convention. Do not run deployments or modify external systems.” Review that proposed adaptation before adopting it.

## Trial request

> Add a profile settings field using the existing form pattern, including failed-save behavior.

Expected behavior: Existing components reused; loading and validation are visible; keyboard use and input preservation are checked.

Try this on an isolated branch or synthetic evidence first. Check actual artifacts and tool results, not just the agent's summary. If it fails, change the narrow instruction responsible and rerun the same scenario. Structural validity alone does not prove behavioral quality.
