# review-changes

Review a defined diff for actionable behavioral defects with concrete evidence. Use for code review requests, not automatic stylistic rewriting.

## Requirements

Git diff or patch, target/base revision, and enough source context to trace behavior. No provider credentials belong in this folder. Configure connectors or CLIs through your coding agent's normal setup. If an integration is unavailable, use supplied evidence or return a local draft with the limitation stated.

## Set up with your coding agent

1. Copy this complete folder into `.agents/skills/review-changes/` for Codex, or `.claude/skills/review-changes/` for Claude Code. Compare and merge if a folder already exists.
2. Let the coding agent inspect this project's own instructions, manifests, examples, and commands before following the skill.
3. Invoke `$review-changes` in Codex or `/review-changes` in Claude Code. For other agents, consult their skill support; when unavailable, attach both Markdown files and explicitly ask the agent to follow them for the task.
4. Keep project-wide policy in your existing project instruction file. Add a short pointer to this skill when useful instead of copying its entire procedure there.

Official setup references: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills).

## Adapt to your project

Configure: **default base discovery; severity scale; protected invariants; test commands; review output preference**. Replace framework or workflow choices only when your repository supports the replacement. Preserve the procedure's evidence requirements and scope boundaries. Remove steps that truly do not apply rather than inventing infrastructure to satisfy them.

Ask your agent: “Inspect this repository and the installed skill before using it. Follow the project's existing conventions and cite the files that establish them. Do not install tools or perform external actions.”

## Trial request

> Review this diff against its actual PR base. Focus on bugs and give line-specific evidence.

Expected behavior: Findings explain a reproducible condition and effect; no speculative style list or automatic publication.

Try this on an isolated branch or synthetic evidence first. Check actual artifacts and tool results, not just the agent's summary. If it fails, change the narrow instruction responsible and rerun the same scenario. Structural validity alone does not prove behavioral quality.
