# Adapt a skill to your own project

Here, “fine-tune” means editing reusable instructions and project context. It does not update model weights.

## Discover before prescribing

Ask your agent to inspect the repository policy, package manifests, CI workflows, two nearby examples, and current tests. Have it propose actual paths and commands for the worksheet, with file references. It should not add libraries, rename branches, create accounts, or change infrastructure just to match a template.

Use this prompt:

> Read the chosen skill and its project-context worksheet. Inspect this repository read-only. Fill in facts you can establish from code, scripts, and CI, citing paths. Leave unknown facts marked unknown and list the few decisions that need me. Then adapt the skill to our existing workflow. Preserve its task boundary; do not install tools or perform external actions.

## Separate three kinds of instruction

**Project policy** belongs in the repository's agent instructions: package manager, architectural boundaries, branch conventions, and what counts as completion.

**Procedures** belong in skills: how to review a change, investigate an error, or prepare a test plan.

**Facts** belong in the worksheet or maintained references: paths to schemas, test fixtures, deployed environments, and exact commands. Store credential names or connector names only, never credential values.

## Choose facts that change decisions

For a frontend skill, identify your components and form behavior. For API work, identify authentication and tenant boundaries. For testing, identify the public module boundary and the real fixture helpers. For deployment, establish which command creates previews and what it publishes. Avoid importing another project's styling preferences or stack as universal rules.

A useful customized rule says: “The save form awaits the mutation and displays a field error without losing user input.” An unhelpful one says: “Always write clean code.” A brittle one hard-codes an obsolete component path with no maintained example.

## Start small

Adapt one skill for one repeated problem. Run it on a small branch, then try an ambiguous task and a task that should not trigger it. Do not turn every incident into a permanent rule. Add a rule when it changes a decision and has a repeatable reason.

Suggested evaluations:

| Skill | Trial | Evidence to inspect |
| --- | --- | --- |
| review-changes | Diff with a cross-tenant lookup | Does it trace authorization and point to the failing path? |
| write-tests | Duplicate webhook bug | Does the test assert one observable effect, rather than helper calls? |
| validate-changes | Shared package edit | Does it include affected consumers without checking every unrelated app? |
| agent-review-loop | Reviewer finds a regression | Does it re-review the changed revision and stop at its round limit? |
| investigate-errors | Browser-extension exception plus app exception | Does it avoid suppressing the real app failure? |
| deploy-preview | Dirty worktree with unrelated changes | Does it identify the intended artifact without committing unrelated work? |

## Adapt for different agents

Use the paths in the root README. Confirm discovery by asking the agent to name the selected skill and summarize its task boundary. Native skills, repository instructions, permissions, and connected tools are different mechanisms. A Markdown file does not grant credentials or make unavailable tools callable.

For agent runtimes without delegation, the review-loop skill supports sequential review but must label the independence limit. Never label a single agent's self-review as an independent reviewer.

## Share responsibly

Before sharing a customized kit, remove company/client names, issue keys, internal URLs, cloud resource identifiers, local user paths, raw logs, customer records, and credential examples. Replace scripts with original generic implementations or documented setup when redistribution rights are unclear. Keep real product claims in your professional context document, not in public templates.

Keep a short local evaluation note: task, revision, expected behavior, observed outcome, and what changed in the skill. Re-test after material changes. Passing a frontmatter validator only verifies packaging, not engineering judgment.
