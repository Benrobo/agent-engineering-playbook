---
name: frontend-performance
description: "Diagnose slow page loads, sluggish interactions, and layout instability with measured evidence. Use for frontend performance work; adapt to the actual framework and browser rather than prescribing a library or optimization checklist."
---

# Frontend performance

Identify the slow user experience before choosing an optimization. Establish the
route, interaction, content volume, device/browser, network, cache conditions,
and build mode. Inspect existing performance budgets and instrumentation. Keep
development overhead distinct from the behavior of a production build.

## Measure the limiting path

Use available profiling tools and project commands. Capture a baseline under
repeatable conditions and relate the metric to what the user experiences.
Inspect request ordering, asset delivery, execution, rendering, and server work
as the evidence requires. Find the dominant cost rather than applying every
possible optimization to every layer.

For a loading issue, identify what blocks useful content. For an interaction
issue, trace work from input to feedback. For a layout shift, find the element
and the late size or content change. Check actual dependency relationships
before parallelizing requests or moving work across runtime boundaries.

## Make a supported change

Change the measured bottleneck in the project's existing architecture. Consider
asset sizing, delivery order, repeated work, subscriptions, or rendering cost
only where the trace supports them. Caching needs a correct ownership and
invalidation model; deferring work must preserve the task's usability. Apply
memoization, virtualization, preload hints, or new dependencies for demonstrated
benefit rather than a fixed component count or framework rule of thumb.

Re-measure under comparable conditions. Use enough samples to distinguish a
change from noise, retain the baseline, and inspect the main task for behavioral
or accessibility regressions. Report regressions and tradeoffs alongside gains.

## Report what was measured

State the metric, scenario, measurement method, before/after evidence, and limits.
Keep synthetic lab results separate from field observations; a loading-only
trace does not establish interaction performance. If tooling or a representative
environment is unavailable, label source-level hypotheses instead of inventing
numbers or claiming that a suspected optimization improved performance.

Metric reference: [Web Vitals](https://web.dev/articles/vitals). Consult current
definitions when interpreting a report; do not treat a single score as a complete
description of the experience.
