---
name: api-contracts
description: "Change API schemas, authorization, handlers, and typed consumers consistently. Use when adding or modifying an endpoint or RPC procedure."
---

# Api Contracts

Read the repository's active instruction files and inspect the relevant code, scripts, and canonical examples before acting. Follow the project's existing conventions and the current task. This procedure does not expand authorization.

## Workflow

1. Trace the request from consumer through input validation, authorization, business logic, and persistence. Identify the established public contract and compatibility requirements.
2. Keep validation, handler behavior, and registration consistent with the project. Reuse the correct authenticated or public base; authentication alone does not prove resource ownership.
3. Update affected client calls, returned types, and error handling together. For generated query/mutation builders, put supported callbacks inside the builder rather than overriding its generated options by object spread.
4. Preserve existing domain logic and test the public boundary, including unauthorized access and invalid inputs when relevant. Do not duplicate types already generated from a schema.
5. Explain any incompatible change and migration requirement. Treat tRPC, REST, GraphQL, or another framework as a project choice, not a reason to rewrite the API.
