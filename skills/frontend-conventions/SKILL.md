---
name: frontend-conventions
description: "Apply existing UI, component, and form conventions while implementing frontend changes. Use for UI behavior and component work, not a wholesale redesign."
---

# Frontend Conventions

Read [project-context.md](project-context.md) for configured facts. Verify stale or missing facts against the repository; do not interpret unconfigured fields as values or permission. Follow the active task and project instructions. This procedure does not expand authorization.

## Workflow

1. Identify whether the target is current or legacy UI and find the nearest maintained example. Reuse existing tokens, components, utilities, and interaction patterns.
2. Keep state near its owner. Subscribe to narrow form fields where supported instead of watching a whole form through every component. Use the project's established API for validation and dirty state.
3. Make pending, empty, failure, and success behavior explicit. Await work that drives loading indicators. Show errors beside the affected input when possible and preserve user input on failure.
4. Avoid redundant success notifications where the updated UI already confirms completion. Preserve accessible labels, keyboard operation, focus behavior, and responsive layouts.
5. Check the real user flow and relevant viewport sizes. Prefer a focused change over migrating legacy areas. Report any inaccessible environment rather than claiming visual verification.
