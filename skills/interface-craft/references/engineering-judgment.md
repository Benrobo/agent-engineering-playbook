# Engineering judgment

Use this when a design suggestion needs qualification. These notes supplement the source review rather than treating every visual preference as a universal standard.

## Accessibility requirements need their actual definitions

WCAG 2.2 AA ordinarily requires pointer targets of at least 24 by 24 CSS pixels, with defined exceptions including spacing and inline text. The painted icon size is not necessarily its activation area. Prefer comfortable controls over designing to the smallest permitted exception. See [W3C target-size guidance](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).

For WCAG AA text contrast, the usual thresholds are 4.5:1 for ordinary text and 3:1 for large text, with defined exceptions. Determine whether the text actually qualifies as large and account for the rendered background. Meeting this criterion alone does not establish accessibility compliance. See [W3C contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

## Diagnose browser workarounds

`will-change` can create layers, consume resources, and affect stacking behavior. Use it only for a demonstrated rendering problem; verify the result on the affected browser and remove it when unnecessary. It is not a global performance switch. See [MDN will-change](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change).

## Project-specific qualifications

- Existing semantic colors may use different names. Preserve a coherent vocabulary rather than renaming the entire project for stylistic agreement.
- A system-theme preference and a user override can coexist if both resolve into one effective theme. Test the resolution logic and persistence instead of introducing competing CSS authorities.
- A shadow cannot substitute for a required focus indicator. Flat, high-contrast, or dense interfaces may need visible boundaries. Preserve clarity in forced-colors environments.
- Font rendering varies by platform. Inspect real text at its intended size; a rasterization preference that makes a heading attractive can make small body text too thin.
- Tight single-line controls still need a strategy for localization and zoom. Do not preserve a preferred shape by clipping essential text.
- An animation should have a purpose and an affordable rendering cost. Repeated interactions and time-sensitive tasks deserve special scrutiny. Do not delay access to content for a decorative sequence.
- A disabled action may be valid during an in-flight request or when permissions prohibit it. Make the reason discoverable; do not change domain permissions to fit a visual convention.
- Web CSS advice does not directly configure native mobile components. For React Native, preserve the design intent using platform APIs and platform accessibility testing; do not claim browser verification covers native behavior.

These are judgment calls to verify in the target product. Record meaningful exceptions in the audit ledger so another reviewer can understand why a recommendation was not followed literally.
