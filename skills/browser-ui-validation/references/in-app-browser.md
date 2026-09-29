# In-app browser handling

Use this reference only when the current environment exposes an in-app browser.
The active tool documentation decides the API. Do not paste a remembered browser
bootstrap path or assume a full Playwright/CDP implementation is available.

In Codex, opening a browser panel and controlling its page are separate
capabilities. A panel-open result does not establish rendered verification.
Discover the available browser-control tool and read its setup instructions.
When `cua_repl` is exposed, respect its first-call rules and use its documented
entry point for the user's tab mention, known tab, or new in-app tab. Retain the
resulting handle while valid; recover a stale tab within the selected browser.

Use the documented accessibility or DOM observation for controls and state.
Use screenshots to evaluate appearance. Refresh element references after page
changes rather than replaying stale indices. Read capability documentation before
using viewport overrides, developer inspection, or screenshot persistence.
Do not assume unsupported methods, inject mutations through a read-only evaluator,
or switch to a separate session to bypass a browser restriction.

For a local application, read the browser's local-development guidance if
provided. Verify the actual server address, route, and build. If the browser
and server run on different hosts, use the environment's supported forwarding
mechanism; localhost alone does not identify the same machine.

Keep research and routine verification in the background. Show the page when
the user asks to watch or inspect it. Restore temporary viewport settings and
use the documented deliverable/handoff mechanism for a preview that should
remain available. Do not close unrelated user tabs or stop their server.

If the browser is unavailable, report what can still be checked from source or
existing tests and what remains visually unverified. Never turn a missing
capability into an invented successful inspection.

Source: [official Browser documentation](https://learn.chatgpt.com/docs/browser),
reviewed 29 September 2026, supplemented by the available runtime documentation.
Availability and API details must be rediscovered in the execution environment.
