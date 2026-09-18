# Three adaptation examples

These are illustrative product types. Confirm your own code and commands before adopting any rule.

## Offline mobile companion

Map frontend conventions to native components, navigation, accessibility labels, keyboard handling, and safe areas. API contracts should describe local/remote synchronization and what remains available offline. Tests should cover a saved note after restart, airplane-mode reading, reconnect conflicts, and subscription-entitlement boundaries. A preview may be a development build; store submission and TestFlight distribution require their own explicit workflow.

## AI research workspace

Map the API skill to provider adapters, background jobs, report storage, and workspace permissions. Use deterministic provider fixtures for tests; distinguish citations from generated claims. Include request failure, partial research, retry/idempotency, credit charging, and cross-workspace access in test plans. Do not make paid provider calls merely because a test fixture is unavailable.

## Brand-content and publishing product

Document brand-context ownership, media storage, generation versions, approvals, and publishing state. Test that one workspace cannot use another's brand assets and that retrying a scheduled post does not publish twice. Read-only investigation can inspect a provider event; replaying it or posting to a social account is a separate action. Previews should use test accounts and unpublicized sample content.

## Build your own map

For each product, record its highest-cost failure and the smallest test that would expose it. Then adapt the relevant skills around those behaviors. Do not start by copying every tool choice from these examples.
