---
name: frontend-conventions
description: "Implement UI behavior, components, and forms using the target project's established design system and state patterns. Use for frontend changes within an existing product, without imposing a framework or redesign."
---

# Frontend conventions

Trace the affected screen through its routes, composition, components, tokens,
and data ownership. Use project instructions and maintained implementations;
verify that an apparent design rule actually reaches this surface. A similarly
named component in another application may belong to a different system.

Reuse the existing component and interaction primitives. Inspect their variants
and extension points before writing substitutes or combining incompatible focus
systems. Extend tokens when the task calls for a new concept; do not replace
libraries or introduce a utility framework to follow this skill.

Keep state with its owner and derive values that need not be stored separately.
Use the project's established form, query, validation, and subscription APIs.
Preserve meaningful navigation state and distinguish it from temporary local
state; not every input belongs in a URL or global store.

Make pending, empty, error, success, and permission behavior understandable where
those states exist. Await work that drives pending indicators, preserve input
on recoverable failure, and guard against duplicate submission or stale responses
when relevant. Errors belong near the affected action or field and need usable
focus/announcement behavior. Updated content may be enough success feedback.

Use the platform's semantics for actions, links, labels, and state. Preserve
keyboard access, focus restoration, paste, autofill, and supported responsive
behavior. Consider long/localized text and content-driven sizing. Preserve the
existing design vocabulary; a minor feature should not rebrand the application.

Verify the flow and consequential states in the actual runtime. For web work,
prefer an available in-app browser unless the user selected another, and inspect
both current page state and screenshots where appearance matters. For native
work, use native facilities. Report unverified behavior when the environment is
unavailable. Choose checks based on the changed behavior rather than a fixed
list of viewports or tools.
