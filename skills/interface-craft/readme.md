# Interface craft

A reusable skill for building clean, distinctive interfaces and reviewing the details that make them feel finished. It combines an original product-design workflow with a linked, complete review index for the public [Interfaces cheat sheet](https://interfaces.dev/cheat-sheet).

The source page was reviewed in full: 61 recommendations across seven sections. This package does not reproduce the site's full text or demos, and is not its paid agent skill. Detailed source review requires access to that public page; the original design and implementation workflow remains usable offline.

## Contents

- `SKILL.md`: agent workflow and reference routing.
- `project-context.md`: project-specific facts to populate.
- `references/source-review.md`: all 61 coverage IDs and audit procedure.
- `references/design-direction.md`: choosing a visual identity suited to the product.
- `references/engineering-judgment.md`: standards, tradeoffs, and exceptions.
- `references/review-protocol.md`: visual, behavioral, and code verification.

## Requirements

A coding agent that can read Markdown, an existing project or clear build brief, and the project's usual development environment. Browser access is needed to inspect source demos and verify rendered web output. No paid subscription, API key, design library, or new framework is required by this skill. Use the libraries already appropriate for your project.

## Install

From the playbook root, use the installer:

```sh
python3 install.py interface-craft --project "/absolute/path/to/your-project" --agent both
```

For a personal installation, replace `--project ...` with `--user`. The installer verifies copied files and preserves different existing installations unless `--replace` is requested. See the root README for cloning, backups, and activation checks.

Alternatively, copy the whole `interface-craft` folder, including its references:

- Codex: `<your-project>/.agents/skills/interface-craft/`; invoke `$interface-craft`.
- Claude Code: `<your-project>/.claude/skills/interface-craft/`; invoke `/interface-craft`.
- Other coding agents: use their supported skill directory, or attach `SKILL.md` and the referenced files and ask the agent to follow them.

Compare and merge if a skill with that name already exists. Keep a single maintained source when sharing between agents. See the [Codex documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code documentation](https://code.claude.com/docs/en/skills) for current skill discovery behavior.

This copy is packaged in the reusable playbook; it has not been automatically installed into every project.

## Adapt it

Ask the agent to inspect your project and populate `project-context.md` with verified paths and commands. Review those facts. Add actual examples of your product's visual identity, not just adjectives. Establish whether the task is a new design or refinement within an existing system.

If you also use a frontend-conventions skill, let it define repository-specific component rules. Use this skill for visual direction, craft decisions, and rendered review. Neither should silently replace the other's scope.

## Example requests

> Use $interface-craft to build the reading screen. It should feel calm and focused, with annotations easy to return to. Follow the existing stack and verify the narrow layout and error state.

> Use $interface-craft to improve this research dashboard. Preserve navigation, make evidence easier to inspect, and explain the one visual idea that makes the result fit this product.

> Use $interface-craft to audit this publishing flow against every applicable cheat-sheet entry. Save the 61-row ledger, implement the highest-impact fixes, and verify the main task.

For Claude Code, replace the dollar-sign invocation with `/interface-craft`.

## Evaluate your adaptation

Try three small tasks before relying on the skill broadly:

1. Add a small screen to an established product. It should fit without rebranding or new dependencies.
2. Create a new product screen from realistic content. It should have a specific visual direction and functional actions, not generic decorative scaffolding.
3. Audit a deliberately flawed flow. It should distinguish functional defects, accessibility issues, and subjective preferences, with evidence and honest coverage limits.

Record the actual outputs and failures. Change the instruction responsible for a demonstrated failure rather than accumulating universal rules.
