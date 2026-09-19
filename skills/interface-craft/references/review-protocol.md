# Review the actual interface

## Visual pass

Inspect a representative wide layout and the narrowest supported layout. Add intermediate widths where the composition changes. Use actual content and a stress sample. Look for unintended scrolling, clipped controls, inconsistent density, displaced overlays, and an unclear primary action.

Review one screen at normal scale before zooming into details. Fix hierarchy and composition before spending time on tiny decorative adjustments. Inspect a second screenshot after changes; a code edit is not proof that the visual issue disappeared.

## Behavior pass

Walk through the primary task from entry to outcome. Repeat the consequential failure case and a retry. Check that entered information survives recoverable errors, pending work is understandable, and success corresponds to actual state. Test back navigation and dismissing an overlay without completing it where relevant.

Use keyboard-only operation, inspect focus after overlays close, and check that content remains usable with enlarged text. If assistive-technology testing is unavailable, say so. Automated checks may identify some issues but cannot confirm whether the experience makes sense.

Exercise supported theme and motion settings and touch interaction when available. Test slow loading and missing data using the project's existing facilities rather than adding production-only workarounds.

## Code and performance pass

Run the repository's relevant lint, type, and behavior checks. Avoid installing a new test stack for a small visual change. Inspect whether the implementation introduces needless dependencies, global selectors, expensive effects, or layout shifts. Use measured evidence when making performance claims.

## Full source audit

When comprehensive polish is requested, complete every row defined in source-review.md. Associate each applicable entry with an actual component, route, or global rule. “Looks fine” is insufficient evidence for something that requires interaction or measurement.

## Finding format

`Impact — location — observed problem — user consequence — proposed correction — verification`

Prioritize broken task completion and inaccessible behavior, then hierarchy and consistency, then fine visual refinement. Do not inflate small style preferences into blockers.

## Completion record

Record the implemented scope, representative viewports, states exercised, checks run, source-audit coverage, and unverified conditions. Never describe planned tests as passed. Keep the user-facing handoff short and link the longer record if one was created.
