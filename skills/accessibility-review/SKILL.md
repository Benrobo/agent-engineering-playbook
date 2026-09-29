---
name: accessibility-review
description: "Investigate and fix accessibility barriers in affected interface flows using semantics, keyboard behavior, and rendered evidence. Use for accessibility requests or changes to controls, focus, forms, and navigation; do not treat this as a certification."
---

# Accessibility review

Start with the task a person needs to complete and the platform they use. Scope
the review to the requested flow or changed controls. Discover the existing
design system and supported platforms before prescribing markup or APIs.

## Trace barriers to a user task

Inspect the implementation and the running interface when available. Check the
relevant semantics, accessible names, state, instructions, error association,
reading order, and keyboard path. Prefer built-in platform controls when they
already provide the required behavior. Custom semantics require the matching
interaction model; adding an ARIA attribute alone does not implement a widget.

Follow focus through opening, using, and dismissing dialogs or menus, including
after validation and asynchronous changes. Check that focus is visible and not
obscured, that necessary controls are reachable, and that status can be understood
without relying solely on color or animation. Announce changes that need it
without duplicating a control's existing accessible feedback.

For affected layouts, check enlarged text, reflow, contrast against actual
backgrounds, target usability, and alternatives to pointer-only gestures.
Consider reduced motion, images, and media where the flow includes them. Use
the project's supported native accessibility APIs for native interfaces; web
inspection does not verify those behaviors.

## Apply and verify a correction

Fix the underlying control, focus sequence, or content relationship at its owner.
Preserve established design-system behavior and regression-test its consumers
when a shared component changes. Avoid broad ARIA additions or replacing a
library control before understanding the problem.

Use available automated checks for detectable issues, then exercise the relevant
keyboard and assistive-technology flow when supported. State which forms of
testing were unavailable. For standards-specific claims, consult the applicable
criterion, version, level, and exceptions before calling something a violation.

Report the barrier, affected task, reproduction, concrete location, and verified
result. Separate confirmed defects from possible issues requiring further
testing. A scan with no findings is not evidence of complete accessibility.

## References

Use the relevant [W3C evaluation guidance](https://www.w3.org/WAI/test-evaluate/)
and [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/) for the target
control. UI review research also included
[web-design-guidelines](https://www.skills.sh/vercel-labs/agent-skills/web-design-guidelines);
its visual preferences are not accessibility requirements.
