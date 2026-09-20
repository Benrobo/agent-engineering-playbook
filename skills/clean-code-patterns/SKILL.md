---
name: clean-code-patterns
description: "Write, refactor, and review understandable, modular code with clear names, deliberate boundaries, restrained abstractions, readable formatting, and useful documentation. Use for cross-language work, with TypeScript guidance when the project uses TypeScript."
---

# Clean code patterns

Use this skill when code should be easier to understand, change, review, or
hand to another developer. It applies to new features, refactors, reviews,
bug fixes, and repository structure decisions. It supplies a way to reason
about code; the repository's own instructions, formatter, linter, architecture,
and language conventions remain authoritative.

## Start with the repository

Before changing code:

1. Read the repository's active instruction files, package manifests, scripts,
   formatter and linter configuration, and the nearest maintained examples.
2. Identify the domain or feature owner, the public boundary, and the checks
   that prove the behavior. In a monorepo, identify the owning app, service,
   or package before choosing a location.
3. Trace one existing path end to end. Learn how this codebase names files,
   exports modules, validates input, handles errors, fetches data, and tests
   behavior.
4. Write a small design sketch in the task notes or your working message:
   behavior, boundary, affected files, and verification. Keep it short enough
   to revise when the code reveals better evidence.

Do not import another project's conventions as universal rules. A local rule
wins when it is documented, consistently used, and still fits the current
task. When local code is inconsistent, follow the nearest maintained example
and call out the inconsistency before broad cleanup.

## Design for understanding

- Give each module, function, and type one coherent reason to change. Split a
  file when its responsibilities or ownership have diverged; keep tiny
  related operations together when splitting would add indirection.
- Keep domain decisions near the domain that owns them. Put transport parsing,
  persistence details, rendering, and provider calls at their existing
  boundaries instead of leaking them through every caller.
- Prefer a small number of explicit data transformations over a long chain of
  clever helpers. Name intermediate values when they explain a business step.
- Design the smallest interface that the caller needs. Add a reusable
  abstraction after a second real use or when it removes a demonstrated source
  of inconsistency. Do not create wrappers, factories, registries, or generic
  utilities for hypothetical future use.
- Keep dependencies flowing in a clear direction. Import a package through its
  supported public surface and avoid reaching into another domain's internals.
- Make invalid states difficult to represent at boundaries. Validate external
  input once, normalize it deliberately, and pass typed values inward.
- Keep side effects visible. A function that reads or writes a database,
  network, filesystem, clock, or process should make that relationship clear in
  its name, signature, module location, or call site.
- Keep control flow easy to scan. Prefer guard clauses for early rejection,
  explicit branches for meaningful states, and named predicates for business
  rules. Simplify nested conditionals before adding another abstraction.

## Names and boundaries

Choose names that tell a new contributor what a value means in its domain.
Use complete, familiar words; retain an abbreviation only when the repository
uses it as a stable domain term. Avoid names such as `data`, `thing`, `misc`,
`helper`, `manager`, or `utils` when a more specific name is available.

Names should describe the role or decision, not the implementation trivia:

```ts
const eligibleRecipients = recipients.filter(canReceiveNotification);
const retryableFailure = classifyFailure(error) === "retryable";
```

Use the project's established casing for files, folders, symbols, and test
names. Do not encode a type into a name (`userString`, `itemsArray`) or add
ceremonial prefixes to interfaces and private members unless the local style
requires it. Keep a file name and its exported symbol easy to associate.

For domain-oriented code, prefer a shape that makes ownership visible:

```text
<surface>/
  <domain>/
    components/   UI owned by the domain
    hooks/        state or query composition owned by the domain
    lib/          domain helpers and adapters
    types.ts      domain types when they are shared within the domain
    index.ts      deliberate public entry point
```

Use only the folders the domain actually needs. A monorepo may instead use
`apps/`, `services/`, and `packages/`, or an entirely different layout. The
decision is to make ownership and dependency direction visible, not to copy a
particular tree.

## TypeScript baseline

When the project uses TypeScript, read its `tsconfig`, compiler version, and
lint rules before applying these defaults:

- Use ES modules and the project's import/export convention. Keep symbols
  private to a module until another module needs them.
- Let the compiler infer obvious local values. Add annotations at public
  boundaries, exported functions, asynchronous results with non-obvious
  shapes, and places where inference would hide an important contract.
- Model meaningful alternatives with discriminated unions or named result
  types. Narrow `unknown` at the boundary instead of spreading casts inward.
- Treat `any` as an explicit escape hatch that needs a local reason and a
  narrow scope. Prefer a real type, `unknown`, or a boundary adapter.
- Prefer plain functions and data when they express the behavior. Use classes
  when identity, lifecycle, encapsulation, or an existing framework contract
  makes them clearer.
- Keep type-only imports, generated files, and public exports aligned with the
  repository's compiler and bundler settings.
- Use the project's formatter for spacing and wrapping. Do not hand-format a
  neighboring file with a different style during an unrelated change.

Read [references/typescript-baseline.md](references/typescript-baseline.md)
when TypeScript-specific choices, module boundaries, or comment forms need
more detail.

## Comments and documentation

Code should explain itself through names, types, structure, and small functions
before comments are added. A comment earns its place when it explains **why**
the code takes a surprising path, states an invariant, documents a constraint
from an external system, or records a deliberate tradeoff.

- Use a short `//` comment for one local implementation fact or a narrow
  workaround. Keep a multiline implementation comment as consecutive `//`
  lines when the idea needs more than one sentence.
- Use `/** ... */` JSDoc for a public API, generated documentation, or a
  non-obvious contract that callers need. Use one line for a genuinely short
  description and a wrapped block when the contract has multiple parts.
- Do not write comments that restate a name, type, or the next line of code.
  Do not add a docstring to every private helper. Do not use decorative boxes,
  narration, or comments that merely signal what the code visibly does.
- Put durable architectural decisions, workflows, and domain explanations in
  the repository's normal documentation when they do not belong beside one
  declaration.
- Follow the repository's policy for TODOs. If none exists, attach a TODO to a
  tracked issue or remove it before the change is considered complete.

Examples:

```ts
/** Returns the signed URL until the provider's short-lived token expires. */
export function createDownloadUrl(file: StoredFile): string {
  return signUrl(file.path, file.expiresAt);
}

// Keep the provider retry separate from the user-facing timeout. The provider
// can succeed after a transient 429 without making the request feel stuck.
const result = await retryProviderCall(loadProfile, { maxAttempts: 2 });
```

If a comment is needed because the code is difficult to understand, first ask
whether a better name, smaller function, or explicit type would remove the
need. Keep the comment when the difficulty comes from a real external or
historical constraint.

## Formatting and readability

Readable formatting creates visual groups:

- keep imports, declarations, setup, core work, and response/cleanup in clear
  sections;
- use the repository's formatter instead of inventing spacing by hand;
- leave enough whitespace for a reviewer to distinguish logical steps;
- wrap long expressions at meaningful boundaries and align with the local
  formatter;
- avoid compressed one-liners when they hide a branch, side effect, or domain
  decision;
- keep related arguments together and use an options object when positional
  arguments become hard to read;
- remove dead code, unused exports, stale comments, and speculative branches.

Do not make an unrelated formatting sweep. Format changed files and any files
the repository's tooling requires, then review the resulting diff for noise.

## Avoiding AI-shaped code

Before finalizing, look for patterns that make code feel generated or harder
to maintain:

- generic wrappers around one call;
- a new abstraction with no second caller;
- vague names repeated across unrelated domains;
- comments that paraphrase the implementation;
- excessive `try/catch`, defensive checks, or options that the caller cannot
  usefully control;
- nested ternaries, long boolean expressions, and clever chaining that hide
  state transitions;
- broad changes made only to make the touched file look uniform;
- inconsistent blank lines, arbitrary grouping, or formatting that fights the
  repository's formatter.

Replace these with the smallest clear shape supported by evidence. Preserve
existing behavior and explain a meaningful tradeoff in the change summary.

## Work and review loop

1. Inspect the project and choose the owning boundary.
2. State the behavior and the smallest coherent design.
3. Implement one vertical slice with names and types that expose the domain.
4. Re-read the diff as a junior-to-mid-level developer encountering it for the
   first time. Remove indirection, unexplained abbreviations, and misleading
   names.
5. Run the formatter, type checker, linter, and focused tests using the
   repository's own commands. Add or update tests at the observable boundary
   when behavior changes.
6. Review the final diff for scope, dead code, accidental public exports,
   comments that should become code, and missing error or empty states.
7. Report the files changed, checks run, and any limitation that prevented a
   useful verification.

For monorepo layout and dependency direction, read
[references/monorepo-shape.md](references/monorepo-shape.md). For choosing
comment forms and writing documentation that helps future readers, read
[references/documentation.md](references/documentation.md).
