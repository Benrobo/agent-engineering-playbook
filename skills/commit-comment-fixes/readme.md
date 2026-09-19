# commit-comment-fixes

Package already implemented PR-comment fixes into traceable commits and optional requested replies.

## Requirements

Local fixes mapped to review-thread IDs, Git, and optional hosting connector for requested replies. No provider credentials belong in this folder. Configure connectors or CLIs through your coding agent's normal setup. If an integration is unavailable, use supplied evidence or return a local draft with the limitation stated.

## Set up with your coding agent

1. Copy this complete folder into `.agents/skills/commit-comment-fixes/` for Codex, or `.claude/skills/commit-comment-fixes/` for Claude Code. Compare and merge if a folder already exists.
2. Let the coding agent inspect this project's own instructions, manifests, examples, and commands before following the skill.
3. Invoke `$commit-comment-fixes` in Codex or `/commit-comment-fixes` in Claude Code. For other agents, consult their skill support; when unavailable, attach both Markdown files and explicitly ask the agent to follow them for the task.
4. Keep project-wide policy in your existing project instruction file. Add a short pointer to this skill when useful instead of copying its entire procedure there.

Official setup references: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills).

## Adapt to your project

Configure: **commit conventions; thread mapping; allowed push target; validation evidence; reply format**. Replace framework or workflow choices only when your repository supports the replacement. Preserve the procedure's evidence requirements and scope boundaries. Remove steps that truly do not apply rather than inventing infrastructure to satisfy them.

Ask your agent: “Inspect this repository and the installed skill before using it. Follow the project's existing conventions and cite the files that establish them. Do not install tools or perform external actions.”

## Trial request

> Commit the two comment fixes already staged; do not push or reply yet.

Expected behavior: Only the authorized fixes enter commits; external state and unrelated edits stay unchanged.

Try this on an isolated branch or synthetic evidence first. Check actual artifacts and tool results, not just the agent's summary. If it fails, change the narrow instruction responsible and rerun the same scenario. Structural validity alone does not prove behavioral quality.
