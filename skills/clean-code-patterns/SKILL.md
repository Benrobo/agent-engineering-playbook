---
name: clean-code-patterns
description: "Improve code readability, names, control flow, and abstraction choices while writing, refactoring, or reviewing code. Follow the repository's language and conventions; use TypeScript guidance only in TypeScript projects."
---

# Clean code patterns

Make the changed behavior easy to follow without imposing a new house style.
Read applicable project instructions, nearby maintained code, and relevant
formatter/compiler configuration. Scale inspection and explanation to the task.

## Make meaning visible

Use names that explain domain roles and outcomes. Retain established vocabulary,
including meaningful abbreviations. Prefer a named intermediate value when it
reveals a decision or separates an effect from a transformation; do not require
one for every expression or awaited call.

Keep related work together. Separate responsibilities when they have different
owners, lifecycles, or reasons to change. Trace actual consumers before extracting
shared code. Repeated syntax alone does not establish a shared contract, and a
single consumer does not disqualify a useful isolation boundary.

Make dependency direction and side effects visible through the existing module
interfaces. Validate untrusted input at the appropriate boundary and preserve
invariants through the paths that can change state. Avoid redundant validation
inside already-established contracts unless another entry path requires it.

## Keep execution understandable

Prefer branches and early returns that reveal meaningful states. Split dense
expressions or callbacks when names would clarify their steps. Do not compress
business decisions into clever chaining or expand simple expressions into
ceremonial helpers.

Handle failure where it can be recovered from or translated correctly. Do not
silently replace failed production work with sample data or a success-shaped
result. Parallelize independent operations only when their failure and resource
semantics remain correct; keep dependent effects ordered. Preserve cancellation,
cleanup, transaction, and retry behavior when refactoring.

Choose functions, classes, and data structures to fit the language and framework.
A wrapper earns its place by translating, isolating, or enforcing something, not
by renaming a call. Avoid factories and registries for hypothetical extensions.

## Comments and formatting

Improve names and structure before adding narration. Document a non-obvious
contract, invariant, tradeoff, or external constraint that readers otherwise
cannot infer. Use the language's documentation conventions, with tags only when
they add useful information. Recheck comments when behavior changes.

Use the project's formatter and keep logical phases readable within its rules.
Avoid unrelated formatting sweeps and arbitrary import or whitespace mandates.
For comment decisions, read [documentation.md](references/documentation.md);
its syntax examples are TypeScript-specific, not cross-language requirements.

For TypeScript work, read [typescript-baseline.md](references/typescript-baseline.md)
when types, imports, or module semantics need attention. For multi-package
ownership, read [monorepo-shape.md](references/monorepo-shape.md). None of these
references prescribes a directory tree for a different project.

## Check the result

Reread the changed path from the caller's perspective. Remove unused exports,
stale explanations, accidental coupling, and indirection that hides the behavior.
Run relevant project checks and meaningful regression coverage. Report any
behavior change or verification gap; readability work should preserve behavior
unless the task asks to change it.
