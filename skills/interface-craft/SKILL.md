---
name: interface-craft
description: Design, implement, and refine clean, distinctive web interfaces with deliberate visual direction and evidence-based craft reviews. Use for new screens, UI redesigns, component polish, or a detailed interface audit; preserve established product conventions unless redesign is requested.
---

# Interface craft

Deliver an interface that suits the product, works through its important states, and has a recognizable visual point of view. A visually attractive screenshot alone is not completion.

Read [project-context.md](project-context.md). Discover missing facts from the project before choosing libraries, fonts, or commands. This skill does not authorize publication, purchases, or unrelated changes.

## 1. Understand the screen

Identify the audience, primary task, information priority, content volume, and surrounding product. Inspect existing screens and components. For an existing product, determine what already works and what the requested change permits you to alter. For a new product, make a brief, explicit design assumption when the brief is incomplete; do not stall over ordinary choices.

Write a short direction before implementation: user task, intended character, composition, type treatment, and one memorable detail. Use [design-direction.md](references/design-direction.md) to make that direction concrete. Avoid producing several competing concepts unless comparison is requested.

## 2. Design with real content

Build around credible product content and actual actions. Establish the information structure before decoration. Decide which content deserves emphasis and which can recede. Include long, short, missing, and error-prone content in the design; a perfect sample is insufficient.

Reuse the project's components and conventions. New dependencies must solve a real gap. Do not rebrand a mature interface to make a small feature look original. For a new design, derive distinction from the subject, content, and interaction rather than a familiar template with different colors.

## 3. Implement a complete slice

Start with one representative user flow and expand the visual system from it. Account for loading, empty, populated, error, success, and permission states where they exist. Ensure primary actions work; label deliberate prototypes clearly. Avoid fake activity, invented social proof, and controls that imply unavailable functionality.

Consult [source-review.md](references/source-review.md) for the complete source-review procedure and all 61 coverage IDs. Read the relevant source sections during ordinary implementation. For a requested comprehensive audit, inspect every entry and keep an applicability ledger; do not silently skip examples because they are visually small.

Consult [engineering-judgment.md](references/engineering-judgment.md) when a visual recommendation conflicts with browser behavior, accessibility, platform conventions, or an existing design system. Reference guidance is not a command to reproduce the source's visual identity.

## 4. Review the rendered result

Use [review-protocol.md](references/review-protocol.md). Inspect the actual interface at representative narrow and wide widths. Exercise the main task and consequential failure states. Review the visual hierarchy separately from the code. Fix the most noticeable weaknesses first, then inspect again.

Use available browser tools and the repository's relevant checks. If rendering or a required environment is unavailable, state exactly which checks remain unverified. Do not claim an accessibility certification from an automated scan or screenshots.

## Handoff

Briefly explain the visual direction, implemented behavior, and what was verified. Include material limitations and the location of the result. For an audit, prioritize findings by user impact with concrete locations and evidence. Keep the detailed 61-entry ledger in a file when useful instead of dumping it into the conversation.

## Source

Inspired by the public [Interfaces cheat sheet](https://interfaces.dev/cheat-sheet), reviewed 18 September 2026. This is an original workflow with a compact source index, not the site's paid skill or a reproduction of its examples. Further sources and applicability notes are linked in the references.
