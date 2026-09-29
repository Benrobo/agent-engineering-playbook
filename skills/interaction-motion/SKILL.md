---
name: interaction-motion
description: "Design, refine, or diagnose UI transitions, gestures, and animation feedback. Use when motion is part of the requested interaction or causes usability problems; adapt to existing tokens, platform, and input methods."
---

# Interaction motion

Identify what the transition communicates, which states it connects, and how
often someone encounters it. Inspect the actual component, gesture or lifecycle,
motion tokens, and supported input methods. Preserve the product's visual
language and use its existing animation facilities.

Choose feedback according to the task. Frequent actions should remain responsive;
occasional transitions can explain hierarchy or spatial relationships. A static
change may already convey enough. Do not add animation simply because an element
can move, or remove useful motion to satisfy a blanket rule.

Keep the interaction interruptible when users can reverse or repeat it. Inspect
open/close races, cleanup, removal from the document, focus ownership, and input
during transitions. Completion of an animation should not substitute for the
actual completion of a request or make a control temporarily inaccessible.

Choose duration, easing, origin, and spring behavior from the existing system
and the interaction's distance and purpose. Use a new value only when the result
justifies it. Avoid universal numeric recipes, mandatory animation libraries,
or a required bounce/blur/press effect for every product.

Provide an understandable state change when motion is reduced or unavailable.
Keep essential information visible after the animation. For gestures, preserve
an appropriate keyboard or simple-control path where needed. Inspect touch and
native behavior using the relevant runtime rather than assuming a mouse test
proves them.

Verify in the rendered interface: normal use, rapid repeated input, reversal,
and affected motion preferences. Slow playback can help diagnose a transition,
but judge responsiveness at normal speed too. Inspect the actual frame or
rendering cost before claiming a performance fix; transform or opacity can be
useful without guaranteeing inexpensive compositing for every surface.

For a review, report evidence and user consequence with concrete locations. For
requested fixes, implement and recheck them. State when feel, device behavior,
or performance remains unverified. Do not create a separate planning/delegation
workflow unless the task calls for it.

Research: [Improve Animations](https://www.ui-skills.com/skills/emilkowalski/improve-animations)
and [Better UI](https://www.ui-skills.com/skills/jakubkrehel/better-ui), reviewed
29 September 2026. This workflow adapts their motion reasoning without copying
exact values or planning-only restrictions.
