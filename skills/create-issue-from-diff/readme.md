# create-issue-from-diff

Draft an issue from the actual behavior in a diff; create it in a tracker only when requested.

## Requirements

Diff and product context; tracker integration only for requested creation. No provider credentials belong in this folder. Configure connectors or CLIs through your coding agent's normal setup. If an integration is unavailable, use supplied evidence or return a local draft with the limitation stated.

## Set up with your coding agent

1. Copy this complete folder into `.agents/skills/create-issue-from-diff/` for Codex, or `.claude/skills/create-issue-from-diff/` for Claude Code. Compare and merge if a folder already exists.
2. Let the coding agent inspect this project's own instructions, manifests, examples, and commands before following the skill.
3. Invoke `$create-issue-from-diff` in Codex or `/create-issue-from-diff` in Claude Code. For other agents, consult their skill support; when unavailable, attach both Markdown files and explicitly ask the agent to follow them for the task.
4. Keep project-wide policy in your existing project instruction file. Add a short pointer to this skill when useful instead of copying its entire procedure there.

Official setup references: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills).

## Adapt to your project

Configure: **tracker destination; issue template; labels; duplication search; acceptance criteria format**. Replace framework or workflow choices only when your repository supports the replacement. Preserve the procedure's evidence requirements and scope boundaries. Remove steps that truly do not apply rather than inventing infrastructure to satisfy them.

Ask your agent: “Inspect this repository and the installed skill before using it. Follow the project's existing conventions and cite the files that establish them. Do not install tools or perform external actions.”

## Trial request

> Draft a tracker issue for this diff, with a concrete problem and acceptance criteria.

Expected behavior: Issue text describes user behavior and measurable outcomes; no invented tracker record.

Try this on an isolated branch or synthetic evidence first. Check actual artifacts and tool results, not just the agent's summary. If it fails, change the narrow instruction responsible and rerun the same scenario. Structural validity alone does not prove behavioral quality.
