# A practical playbook for coding agents

Reusable Markdown skills for taking software work from an issue to a tested, reviewable change. Each skill is independently adaptable. This kit contains procedures, not a trained model, a guarantee of correctness, or an autonomous production operator.

The skills are reusable procedures. The coding agent already receives project context from the repository and its normal instruction files, so the skills stay portable across projects.

Start with **implement-issue**, **write-tests**, **validate-changes**, and **review-changes**. Add the other workflows when you need them. You do not need every integration to use the core kit.

## Structure

Every folder under `skills/` contains:

- `SKILL.md`: the instructions the coding agent loads.
- `readme.md`: requirements, installation, customization, and a trial request.
- optional `references/`, `scripts/`, and other resources used only by that skill.

The [customization guide](CUSTOMIZE.md) explains how to adapt the kit. The [project policy template](templates/AGENTS.template.md) ties installed skills together. [Project examples](examples/project-adaptations.md) show three different product types without imposing a stack.

## Install a skill into your project

Requirements: Python 3.9+ and a local copy of this playbook. Git is needed only for the clone step. No Python packages are required. Read the skill before installing it.

Run this from the playbook folder, replacing the project path:

```sh
python3 install.py interface-craft --project "/absolute/path/to/your-project" --agent both
```

This actually installs and verifies the complete skill in both agent discovery folders:

- Codex: `your-project/.agents/skills/interface-craft/`
- Claude Code: `your-project/.claude/skills/interface-craft/`

Choose `--agent codex` or `--agent claude` if you use one agent. Install several skills by listing their names:

```sh
python3 install.py write-tests review-changes --project "/absolute/path/to/your-project" --agent codex
python3 install.py --list
```

The project directory must already exist. The installer copies the skill and its supporting files, checks required metadata, compares file hashes, and prints the exact destination and invocation. It does not add project files, execute skill scripts, modify application code, or install every skill automatically.

## Clone, then install

When this playbook is published in Git, substitute its real repository URL below. There is no published URL configured in this local package yet. Cloning downloads the source; the installer performs agent setup.

```sh
git clone "YOUR_REPOSITORY_URL" "$HOME/agent-engineering-playbook"
python3 "$HOME/agent-engineering-playbook/install.py" interface-craft --project "/absolute/path/to/your-project" --agent both
```

If you downloaded the ZIP instead, extract it and run the same installer from the extracted folder. The installed skill is a standalone copy and does not depend on keeping the clone or ZIP extraction in place.

## Personal installation

To make a skill available across your local projects:

```sh
python3 install.py interface-craft --user --agent both
```

This uses `~/.agents/skills/` for Codex and `~/.claude/skills/` for Claude Code. Project and personal locations are documented by [OpenAI](https://learn.chatgpt.com/docs/build-skills) and [Anthropic](https://code.claude.com/docs/en/skills). Avoid installing the same skill at multiple scopes unless you intend the agent-specific discovery behavior.

## Verify, update, and remove

Preview destinations without writing:

```sh
python3 install.py interface-craft --project "/absolute/path/to/your-project" --agent both --dry-run
```

An identical installation is a verified no-op. Different existing files are preserved unless you explicitly use `--replace`; that option saves a backup outside the skill discovery directory before replacing the installed copy. Review local customizations first:

```sh
python3 install.py interface-craft --project "/absolute/path/to/your-project" --agent both --replace
```

After installation, open the target project and invoke `$interface-craft` in Codex or `/interface-craft` in Claude Code. Ask it to describe the loaded workflow before a first real task. If missing, restart the agent and check workspace trust, skill settings, and the printed path. File installation is verified by the script; actual agent activation must be verified in that agent.

The coding agent should inspect the target project's own instructions and source before using an installed skill. If a durable project convention changes the procedure, update that local installed `SKILL.md`; keep the distributable source generic. Future replacements preserve local skill edits in a backup. To uninstall, move that skill folder out of the discovery directory or remove it after preserving changes you need. Do not remove the entire skills directory.

For other agents, use their documented skill location or attach `SKILL.md` and its referenced files directly. This installer supports Codex and Claude Code only.

## Customize before relying on it

1. Read the chosen skill's `readme.md`.
2. Let the coding agent inspect the target project's own instructions, manifests, examples, and commands before using the skill. It already has the project context.
3. Update only the local installed `SKILL.md` when a durable project convention materially changes the procedure. Keep the distributable source generic.
4. Merge the relevant parts of `templates/AGENTS.template.md` into your existing project instructions. Do not replace established rules wholesale.
5. Trial the skill on a disposable branch with a real small task. Compare the result against acceptance criteria and recorded checks.

The kit deliberately contains no credential profiles, organization IDs, internal domains, production connection strings, or automatically executable deployment scripts. Supply integrations through your agent's normal connector or CLI configuration; do not paste credentials into Markdown.

## Skill index

| Skill | Intended job |
| --- | --- |
| [implement-issue](skills/implement-issue/readme.md) | Turn a scoped issue into an implemented change |
| [interface-craft](skills/interface-craft/readme.md) | Design and polish distinctive interfaces with a complete source-review workflow |
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

The content is written as generic, independently adaptable guidance. No company repository, scripts, or private payloads are included. Review your custom additions before sharing the folder on X or elsewhere. Installation is explicit and selective; the installer only installs the skills and scope you name.
