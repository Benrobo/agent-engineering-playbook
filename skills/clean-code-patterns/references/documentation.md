# Documentation and comments

Use this reference when deciding whether code needs a comment, API documentation,
a readme, or a design note. Syntax below illustrates TypeScript; use the target
language's documentation conventions elsewhere.

## Decide whether to write prose

Ask what a future reader would still misunderstand after reading the names,
types, and control flow. If the answer is “nothing,” leave the comment out. If
the answer is a surprising why, an invariant, an external limitation, or a
public contract, write the smallest durable explanation.

| Situation                                        | Preferred form                                       |
| ------------------------------------------------ | ---------------------------------------------------- |
| One local implementation fact                    | `//` line comment                                    |
| A local explanation spanning several lines       | consecutive `//` lines, indented with the code       |
| Exported API contract or generated documentation | `/** ... */` JSDoc                                   |
| A short public description                       | single-line JSDoc                                    |
| Multiple constraints, parameters, or examples    | multiline JSDoc with only useful tags                |
| Architecture, workflow, or product decision      | repository documentation or decision record          |
| Future work                                      | tracked issue or the repository's approved TODO form |

## Good comments

```ts
/**
 * Treats an event as expired at the exact deadline, using the provider's
 * timestamp precision. The caller supplies the clock for deterministic replay.
 */
export function isExpiredEvent(event: ProviderEvent, now: Date): boolean {
  return event.expiresAt <= now;
}

// Claim and record the event atomically so concurrent retries cannot both
// perform the durable change.
await eventStore.applyOnce(event.id, change);
```

The first comment documents a caller-facing contract. The second records a
constraint that the control flow alone would not reveal.

## Weak comments

```ts
// Loop through users
for (const user of users) {
  // Add the name
  names.push(user.name);
}
```

The code already says this. Improve the name or structure if the operation is
hard to follow. Do not preserve a comment merely because it existed before a
refactor; re-check whether it still explains a non-obvious fact.

## JSDoc discipline

Document stable public behavior, units, constraints, failure modes, and
side-effects that callers need. Skip `@param` and `@returns` tags that merely
repeat a clear name and type. Keep examples short and executable when they
are included. Update JSDoc in the same change as the signature or behavior it
describes.

The repository's own documentation generator, lint rules, and comment policy
take precedence over this table.

## Sources

The distinction between JSDoc for documentation and ordinary comments for
implementation details follows the [Google TypeScript Style Guide's comments
guidance](https://google.github.io/styleguide/tsguide.html#comments). Its
examples also cover short and multiline JSDoc and explain why comments should
add information instead of restating code.
