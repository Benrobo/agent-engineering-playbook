# Focused craft decisions

Use this for polish within a product. Find the governing tokens, variants, and
composition before judging a difference. Follow the rendered/import path rather
than grouping unrelated screens because they look similar in a file search.
Design documentation can describe a future direction; verify its current scope.

## Decide what needs attention

Separate a confirmed task barrier, an inconsistency with the local design system,
and a subjective proposal. A screenshot can reveal hierarchy or clipping; source
can establish which style reaches a component. Neither alone proves all behavior.
Recheck a candidate against intentional variants and actual runtime conditions.
Report no finding when the evidence does not support one.

Fix composition before decorative details. Group related content, make the next
useful action discoverable, and choose density for the task. Compare realistic
content at relevant widths. An empty state should explain the situation and
provide a useful next step when one exists; do not invent an action merely to
fill space. Loading feedback should fit the operation and avoid disruptive
changes in geometry.

For detailed refinement, judge nested shapes, optical alignment, icon weight,
surface boundaries, number alignment, and text wrapping at the rendered size.
Use existing tokens and assets when they fit. A radius formula, shadow recipe,
font ban, or single-accent rule is not a universal product requirement. Preserve
structure and focus indicators when changing borders or elevation.

## Motion and state

Motion should communicate a transition, relationship, or response. Consider how
often the user encounters it and whether it delays the next action. Test rapid
reversal, interruption, repeated activation, and reduced-motion behavior for
affected interactions. Keep state understandable after motion finishes or when
motion is absent. Prefer existing motion tokens; derive any new values from the
interaction and verify them rather than copying another product's exact timing.

Treat layout measurements, blur, and layer-promotion hints as performance choices
to measure. Do not claim that a property is always cheap or add a global rendering
workaround to address a local symptom.

## Scope and delivery

An audit can end with supported findings; a plan should identify owners, current
evidence, expected behavior, and how to verify it. If implementation is requested,
make the scoped fixes and inspect the result. Do not impose a fixed findings
count, require another agent, or stop at a plan solely because a source skill does.

Research reviewed 29 September 2026:
[Improve UI](https://www.ui-skills.com/skills/ibelick/improve-ui),
[Baseline UI](https://www.ui-skills.com/skills/ibelick/baseline-ui), and
[Better UI](https://www.ui-skills.com/skills/jakubkrehel/better-ui).
This is an original synthesis. Their stack mandates, exact visual recipes, and
workflow restrictions are not imported as requirements.
