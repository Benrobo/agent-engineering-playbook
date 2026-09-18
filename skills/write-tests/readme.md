# write-tests

Write behavior-focused regression tests at the narrowest useful public boundary. Use when adding coverage for a change or reproducing a bug.

## Requirements

Test runner, representative tests, fixture conventions, and isolated test dependencies. No provider credentials belong in this folder. Configure connectors or CLIs through your coding agent's normal setup. If an integration is unavailable, use supplied evidence or return a local draft with the limitation stated.

## Set up with your coding agent

1. Copy this complete folder into `.agents/skills/write-tests/` for Codex, or `.claude/skills/write-tests/` for Claude Code. Compare and merge if a folder already exists.
2. Populate `project-context.md` using verified project facts. Keep `SKILL.md` and that file together.
3. Invoke `$write-tests` in Codex or `/write-tests` in Claude Code. For other agents, consult their skill support; when unavailable, attach both Markdown files and explicitly ask the agent to follow them for the task.
4. Keep project-wide policy in your existing project instruction file. Add a short pointer to this skill when useful instead of copying its entire procedure there.

Official setup references: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills).

## Adapt to your project

Configure: **test command; public boundaries; fixture factories; test database lifecycle; mock conventions**. Replace framework or workflow choices only when your repository supports the replacement. Preserve the procedure's evidence requirements and scope boundaries. Remove steps that truly do not apply rather than inventing infrastructure to satisfy them.

Ask your agent: “Inspect my repository and propose project-specific edits to this skill and its context worksheet. Cite the files that establish each command and convention. Do not run deployments or modify external systems.” Review that proposed adaptation before adopting it.

## Trial request

> Write a regression test for duplicate webhook delivery crediting an account twice.

Expected behavior: The test exercises the public handler and proves one durable credit after repeated delivery.

Try this on an isolated branch or synthetic evidence first. Check actual artifacts and tool results, not just the agent's summary. If it fails, change the narrow instruction responsible and rerun the same scenario. Structural validity alone does not prove behavioral quality.
