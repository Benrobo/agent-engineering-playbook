# Monorepo shape and domain ownership

Use this reference when deciding where a feature belongs in a multi-package
repository. The layout is a decision aid; the target repository's own
architecture wins.

## Make ownership visible

Start from the deployable surface or runtime that owns the behavior. A common
shape is:

```text
apps/       deployable products or user-facing surfaces
services/   long-running backends, workers, or domain runtimes
packages/   code genuinely shared by more than one consumer
```

Keep a feature's UI, state composition, adapters, and local types together when
that makes the domain easier to find. A common domain shape is:

```text
<domain>/
  components/
  hooks/
  lib/
  types.ts
  index.ts
```

Create only the directories that have a real owner and more than one useful
neighbor. A single five-line helper does not need its own `lib` folder.

## Backend boundaries

When a backend uses layers, keep their responsibilities distinct:

```text
route or handler -> boundary validation -> controller/use case -> service -> persistence/provider
```

The exact names vary. The useful questions are:

- Where is external input parsed and normalized?
- Where is authorization decided?
- Where is the domain rule expressed?
- Which module owns persistence or provider details?
- Which result shape is safe for the caller?

Do not move logic between layers only to match this diagram. Follow the
repository's established path and keep a change local when the current shape
already communicates ownership.

## Shared packages

Promote code into a shared package when multiple consumers need the same
stable contract or behavior. Keep it local when one surface owns it. Before
adding a shared export, inspect its consumers, runtime compatibility, and
release/build boundary. Shared code should not import app internals.

Use a package's public entry point when one exists. Reaching into another
package's private directory couples the code to file layout and makes future
refactors expensive.

## Reference pattern observed in Elorah

The Elorah repository demonstrates this reasoning with deployable surfaces in
`apps/`, runtime code in `services/`, and shared contracts or UI in
`packages/`. Its admin UI groups domains under `modules/<domain>/` and commonly
keeps components, hooks, and small domain helpers together. Its engine makes
transport, validation, controllers, services, and persistence easy to locate
through file suffixes and directories. Its repository instructions and memory
files document the architecture, conventions, and recurring recipes before an
agent edits code.

Use the lesson rather than the literal names: a reader should be able to find
the owning domain, follow the main data path, and tell which modules are safe
to reuse.
