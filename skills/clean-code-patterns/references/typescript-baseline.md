# TypeScript baseline

Use this reference when a task needs a TypeScript-specific decision. Start by
reading the target repository's compiler and lint configuration. These are
defaults for reasoning, not a license to reformat or migrate an existing code
base.

## Modules and exports

Use the project's ES module convention and keep each module's public surface
deliberate. Export a symbol when another boundary needs it; keep implementation
helpers private. Prefer named exports when the repository uses them because
they make the dependency visible and reduce accidental default-export churn.
Respect a repository that has a different established export convention.

Avoid global namespaces and hidden side effects. A file with an import or
export is a module; use module boundaries instead of relying on shared globals.
Keep import paths and type-only imports compatible with the configured module
resolution and runtime.

## Types and control flow

- Infer simple locals and annotate public contracts, callbacks whose shape is
  not obvious, and values crossing a package or process boundary.
- Use discriminated unions for states with different required data:

  ```ts
  type LoadResult<T> =
    | { status: "success"; value: T }
    | { status: "empty" }
    | { status: "error"; message: string };
  ```

- Narrow `unknown` once at an input boundary. Keep a cast close to the
  evidence that justifies it and avoid using a cast to silence a design issue.
- Prefer a domain type over a record with arbitrary string keys when the set of
  values is meaningful. Use an options object when a call has several related
  optional values or booleans.
- Do not introduce a class only to hold stateless functions. Use a class when
  identity, lifecycle, encapsulation, or a framework contract makes it clearer.
- Keep async work visible in names and signatures. Decide explicitly how the
  caller observes loading, failure, cancellation, retry, and partial success.

## Names

Use the repository's casing and file suffixes. Names should express the domain
role (`eligibleRecipients`, `parseWebhookEvent`, `NotificationPolicy`) rather
than a vague container (`data`, `helper`, `manager`). Do not add `I` prefixes or
type suffixes unless the project already relies on them for a meaningful
reason. Avoid abbreviations outside stable domain vocabulary.

## Formatting

Run the configured formatter. The important invariant is a consistent visual
rhythm: imports grouped as the tool expects, one blank line between logical
sections when the formatter permits it, wrapped calls at argument boundaries,
and enough whitespace to see state transitions. Do not hand-tune a single file
against a repository-wide formatter.

## Sources

- [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html)
- [TypeScript Handbook: Modules](https://www.typescriptlang.org/docs/handbook/2/modules.html)
- [TypeScript Design Goals](https://github.com/microsoft/TypeScript/wiki/TypeScript-Design-Goals)
