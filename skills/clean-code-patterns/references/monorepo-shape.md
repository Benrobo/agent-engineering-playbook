# Ownership across packages

Use this when a task crosses package or runtime boundaries. Discover the actual
workspace layout, package exports, build graph, and release boundaries. Folder
names alone do not establish ownership or dependency direction.

Trace who owns the behavior, which consumers need it, and whether those consumers
can share a runtime contract. UI, command-line, worker, and server code may share
a schema while needing different implementations. Keep private clients and
privileged runtime dependencies out of consumer bundles that cannot use them.

Promote code when real consumers need stable shared behavior or a deliberate
isolation boundary. Check whether the code has the same reason to change in each
consumer. Prefer an existing owner and public export over a new shared package
when that preserves cohesion. Do not reach through another package's private
layout merely to avoid defining the needed interface.

Keep dependency construction compatible with the repository's lifecycle. Avoid
cycles in which domain code imports a composition root that already imports it.
Separate content construction from loading or delivery where it gives useful
reuse or tests; do not create forwarding layers solely to fill an architecture
diagram.

A structural change should be explainable in terms of ownership, consumers,
compatibility, and verification. Check affected callers and builds after moving
code. Do not impose a domain-first or layer-first layout, generate standard
folders, or migrate unrelated packages to satisfy a template.
