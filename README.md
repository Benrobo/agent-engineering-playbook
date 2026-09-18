# A practical playbook for coding agents

Reusable Markdown skills for taking software work from an issue to a tested, reviewable change. Each skill is independently adaptable. This kit contains procedures, not a trained model, a guarantee of correctness, or an autonomous production operator.

Start with **implement-issue**, **write-tests**, **validate-changes**, and **review-changes**. Add the other workflows when you need them. You do not need every integration to use the core kit.

## Structure

Every folder under `skills/` contains:

- `SKILL.md`: the instructions the coding agent loads.
- `readme.md`: requirements, installation, customization, and a trial request.
- `project-context.md`: a short worksheet for that skill's project-specific facts. Populate it from your repository; an empty field is unknown, not permission to guess.

The [customization guide](CUSTOMIZE.md) explains how to adapt the kit. The [project policy template](templates/AGENTS.template.md) ties installed skills together. [Project examples](examples/project-adaptations.md) show three different product types without imposing a stack.

## Install one skill

From the root of the project you want to improve, copy a chosen folder. These commands assume the downloaded playbook is in a sibling directory. Adjust that source path before running. If the destination already exists, compare and merge it rather than replacing it.

```sh
mkdir -p .agents/skills
cp -R ../agent-engineering-playbook/skills/review-changes .agents/skills/review-changes
```

For Codex, repository skills live in `.agents/skills/<name>/SKILL.md`; invoke a skill explicitly as `$review-changes` or let its description guide discovery. See [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

For Claude Code, copy into `.claude/skills/<name>/` and invoke `/review-changes`. Keep one maintained source if you use both agents. See [Claude Code skills](https://code.claude.com/docs/en/skills).

For another coding agent, check its own current skill support. If it does not load `SKILL.md`, attach that file and its populated `project-context.md` to the task and explicitly ask it to follow them. Do not assume it scans either directory.

## Customize before relying on it

1. Read the chosen skill's `readme.md`.
2. Fill its `project-context.md` with verified paths, commands, and tool availability.
3. Edit `SKILL.md` where your project's behavior or workflow differs. Keep the trigger narrow.
4. Merge the relevant parts of `templates/AGENTS.template.md` into your existing project instructions. Do not replace established rules wholesale.
5. Trial it on a disposable branch with a real small task. Compare the result against acceptance criteria and recorded checks.

The kit deliberately contains no credential profiles, organization IDs, internal domains, production connection strings, or automatically executable deployment scripts. Supply integrations through your agent's normal connector or CLI configuration; do not paste credentials into Markdown.

## Skill index

| Skill | Intended job |
| --- | --- |
| [implement-issue](skills/implement-issue/readme.md) | Turn a scoped issue into an implemented change |
| [frontend-conventions](skills/frontend-conventions/readme.md) | Follow the project's UI and form patterns |
| [api-contracts](skills/api-contracts/readme.md) | Change API validation, handlers, and consumers together |
| [write-tests](skills/write-tests/readme.md) | Test behavior and regressions at useful boundaries |
| [validate-changes](skills/validate-changes/readme.md) | Run checks appropriate to the changed surfaces |
| [review-changes](skills/review-changes/readme.md) | Review a defined diff with evidence |
| [agent-review-loop](skills/agent-review-loop/readme.md) | Bound repeated review and fixes |
| [generate-test-plan](skills/generate-test-plan/readme.md) | Map a diff to user workflows and manual checks |
| [address-pr-comments](skills/address-pr-comments/readme.md) | Triage comments and implement scoped local fixes |
| [commit-comment-fixes](skills/commit-comment-fixes/readme.md) | Commit fixes and, when requested, reply with evidence |
| [create-issue-from-diff](skills/create-issue-from-diff/readme.md) | Draft or create a ticket reflecting the actual change |
| [pr-ready](skills/pr-ready/readme.md) | Assemble checks, review, and PR handoff |
| [publish-review-receipt](skills/publish-review-receipt/readme.md) | Record exactly which revision was reviewed |
| [deploy-preview](skills/deploy-preview/readme.md) | Deploy a requested preview of a known revision |
| [investigate-errors](skills/investigate-errors/readme.md) | Separate product failures from telemetry noise |
| [audit-slow-queries](skills/audit-slow-queries/readme.md) | Relate measured database load to application code |
| [investigate-integration](skills/investigate-integration/readme.md) | Trace provider events through local state and business rules |

## What counts as success

A skill should reduce repeated explanation and improve observable task outcomes. Useful evidence includes a reproduced bug, a failing-then-passing regression test, a review finding tied to a real code path, or a preview verified at the intended revision. A model saying “looks good” is not validation.

The content is written as generic, independently adaptable guidance. No company repository, scripts, or private payloads are included. Review your custom additions before sharing the folder on X or elsewhere. This kit has not been installed into your projects automatically.
