# clean-code-patterns

Write and review understandable, modular code with clear names, deliberate
boundaries, restrained abstractions, readable formatting, and documentation
that adds real information. The skill is language-aware without being tied to
a framework; its TypeScript guidance is the strongest when the repository uses
TypeScript.

## Requirements

A coding agent that can read the repository, its instruction files, source,
formatter/linter configuration, and normal test commands. No framework,
provider, credential, or new dependency is required.

## Set up with your coding agent

1. Copy this complete folder into `.agents/skills/clean-code-patterns/` for
   Codex, or `.claude/skills/clean-code-patterns/` for Claude Code. The root
   playbook installer can do this for you.
2. Let the coding agent inspect the target repository's instructions,
   manifests, package boundaries, representative code, formatter, linter, and
   tests before using the skill.
3. Invoke `$clean-code-patterns` in Codex or `/clean-code-patterns` in Claude
   Code. For another agent, use its supported skill directory or attach this
   folder and ask it to follow `SKILL.md`.
4. Keep the repository's own conventions authoritative. The skill improves
   decisions about names, boundaries, abstractions, comments, and review; it
   does not replace project policy or language tooling.

Official discovery references: [Codex skills](https://learn.chatgpt.com/docs/build-skills)
and [Claude Code skills](https://code.claude.com/docs/en/skills).

## Adapt to your project

Ask the agent to identify the nearest maintained examples and the commands that
format, lint, type-check, test, and build the affected surface. If the project
has a monorepo, ask it to map package ownership and allowed dependency
direction before adding a file. Preserve the skill's principles while using
the project's actual naming, import, error, test, and documentation rules.

Prompt:

> Use `$clean-code-patterns` for this task. Read the repository instructions
> and two nearby examples first. Choose the owning domain and smallest clear
> design, follow the existing formatter and naming conventions, add comments
> only for non-obvious why or constraints, and run the focused checks. Explain
> any tradeoff that affects future reuse.

## Trial request

> Refactor this feature so a junior-to-mid-level developer can follow the main
> path. Keep behavior unchanged, preserve the repository's conventions, avoid
> speculative abstractions, improve names and file boundaries only where the
> evidence supports it, and report the checks you ran.

Expected behavior: the agent inspects local patterns, changes the smallest
coherent surface, keeps domain ownership visible, avoids generic helper
proliferation, uses comments selectively, and verifies behavior with the
project's own tooling.

## Evidence behind the TypeScript guidance

The TypeScript-specific defaults were checked against the [Google TypeScript
Style Guide](https://google.github.io/styleguide/tsguide.html), the [TypeScript
Handbook's modules guide](https://www.typescriptlang.org/docs/handbook/2/modules.html),
and the [TypeScript contributor coding guidelines](https://github.com/microsoft/TypeScript/wiki/Coding-guidelines).
Those references inform the skill; local project rules still decide the final
format and architecture.
