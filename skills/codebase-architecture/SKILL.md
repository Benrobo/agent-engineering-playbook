---
name: codebase-architecture
description: "Infer code ownership and dependency boundaries when placing new behavior, extracting shared code, or reviewing a structural change. Adapt to the repository's language and architecture without imposing a folder layout."
---

# Codebase architecture

Make it clear where behavior belongs and which code may depend on it. Infer
the architecture from working code and project instructions; a proposed design
document is evidence of intent, not proof that a package or interface exists.

## Find the owner

Trace a representative path for the task: entry point, decisions, state or
effects, and consumers. Read relevant manifests, dependency declarations,
public interfaces, and maintained neighboring implementations. Distinguish
current conventions from generated code, migrations, and abandoned patterns.
Investigate only as far as the placement or dependency decision requires.

For each addition, identify what it means, who changes it, and who consumes it.
A constant can express policy, content, configuration, or a protocol value;
its syntax does not determine its owner. Keep single-use behavior local unless
an existing framework boundary or lifecycle gives it a better home.

## Choose the smallest coherent boundary

- Extract when responsibilities diverge, a contract needs isolation, or real
  consumers need the same behavior. Similar-looking code with different reasons
  to change may be clearer kept separate.
- Cross-domain use does not erase domain ownership. Pass the needed value or
  use an owned interface instead of importing another domain's private state.
- A folder or package should express a cohesive responsibility, runtime,
  lifecycle, or public interface. Follow established layouts; neither a fixed
  file count nor a ban on names such as services or modules determines quality.
- Keep public surfaces deliberate. Check actual callers, runtime compatibility,
  build rules, and dependency direction before exporting or promoting code.
  Avoid cycles and importing privileged dependencies into unprivileged runtimes.
- Choose functions, classes, modules, and dependency construction to fit the
  language and project. Add an adapter when it translates or isolates a real
  boundary, not simply to forward every underlying call.

## Separate decisions from delivery where it helps

Keep business invariants at a boundary all relevant callers use, including
background work. A transport handler's authentication check may not enforce
resource ownership for an internal caller. Follow the project's established
authorization and transaction model rather than inventing a parallel one.

Distinguish external clients, configuration, policy, and content when their
consumers or lifecycles differ. A template or prompt builder can accept prepared
inputs without loading data or sending messages. Keep this separation local
when a separate package or provider hierarchy would add no value.

For UI work, place state and behavior with their actual owner. Shared components
should receive a useful contract rather than depend on feature internals.
Routing, persistence, and feature composition follow the framework's existing
boundaries; browser, native, server-rendered, and static interfaces need not
have the same structure. Distinguish fixture content from production behavior.

## Keep formatting and execution readable

Read the owning package's formatter, linter, and language conventions before
changing code. Follow their import order, indentation, quoting, and wrapping;
avoid manual alignment or unrelated formatting sweeps.

- Keep imports at the language's conventional module boundary. Use deferred or
  dynamic imports for a real loading, runtime, or dependency constraint, not to
  conceal dependencies inside expressions.
- Name meaningful intermediate results when they expose a domain step or make
  asynchronous work easier to follow. Separate loading, transformation, and
  response construction when nesting obscures them; avoid mechanical temporary
  variables for already-clear expressions.
- Use whitespace to distinguish validation, effects, transformation, and cleanup
  without separating every related statement. Let the formatter wrap long calls
  and component properties.
- Prefer readable branches and guard clauses over compressed conditions with
  hidden effects. Name handlers when they perform several meaningful steps;
  group arguments when positional values become ambiguous.
- Preserve ordering, error propagation, and cleanup while improving readability.
  Parallelize only independent work. Do not mechanically remove an awaited
  return when the surrounding error handling depends on it.

## Document contracts and decisions where they belong

Improve unclear names and control flow before adding comments. Document what a
caller or maintainer cannot otherwise infer: responsibility, lifecycle,
ownership, ordering, side effects, units, failure modes, or an external constraint.
Do not add documentation to every ordinary component, getter, or CRUD operation.

Use the language's documentation form for a non-obvious declaration or public
contract, and a nearby implementation comment for a local reason or invariant.
For JavaScript or TypeScript, this generally means a multiline `/** ... */`
block for a substantial contract and consecutive `//` lines for an implementation
explanation; follow established tooling and project conventions. Other languages
should use their own supported forms rather than copying this syntax.

Write plain sentences that explain why the behavior matters. Use parameter,
return, failure, or example documentation only when it adds meaning beyond the
signature. Examples should show valid usage and necessary assumptions; document
only guarantees the implementation actually provides. Explain a class's overall
responsibility once and a method's particular contract where needed.

Keep local explanations beside the relevant decision. Put decisions spanning
multiple modules in the repository's usual architecture documentation when they
need a durable explanation. Avoid decorative dividers, narration of obvious
operations, and comments used to excuse avoidable complexity. Update or remove
comments and examples when behavior or ownership changes.

## Verify the choice

Inspect imports and callers after the change. Verify public contracts and
affected runtime/build boundaries using the repository's relevant checks.
Run relevant formatting checks and confirm that comments still describe the
implemented behavior rather than a proposed design.
Explain a consequential ownership decision with evidence from the code; an
ordinary local addition does not need a separate architecture document.
Do not migrate untouched areas to make them match an inferred ideal.
