---
name: deploy-preview
description: "Deploy a requested preview using the repository configured provider and verify the resulting artifact and URL."
---

# Deploy Preview

Read the repository's active instruction files and inspect the relevant code, scripts, and canonical examples before acting. Follow the project's existing conventions and the current task. This procedure does not expand authorization.

## Workflow

1. Inspect the existing deployment configuration and confirm the intended project and preview environment. Do not guess an account or production target.
2. Record the revision and whether local uncommitted files will enter the deployment. Check required build inputs and environment variable names without exposing secret values.
3. Build or deploy using the established workflow within the user's requested scope. Do not commit all changes or push automatically as a shortcut.
4. On failure, inspect the concrete cause before retrying; stop if the same external blocker recurs. Do not alter production settings or broaden access to repair a preview.
5. Verify the returned URL, deployment identity, and relevant route or behavior. Distinguish an HTTP response from a functional end-to-end check. Report the included revision/local state and remaining verification limits.
