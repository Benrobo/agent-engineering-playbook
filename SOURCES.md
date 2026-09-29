# Skill research and adaptation

Reviewed 29 September 2026. These sources informed original, portable workflows.
No third-party skill package, executable, or paid resource was vendored. Links
identify the reviewed sources; they are not required runtime dependencies.

## Architecture extraction

The user-supplied architecture skill and formatting reference were read in full.
Retained: ownership by meaning, deliberate public boundaries, real consumers,
runtime separation, content/effect separation, readable execution, useful
contract and implementation comments, project-aware formatting, and
proportionate verification.
Removed: private project identity, prescribed frontend/backend trees, specific
frameworks and icon libraries, mandatory classes, folder-name bans, formatter
values, and universal intermediate-variable/comment syntax rules. The resulting
codebase-architecture skill discovers conventions from the target repository.

## Public skills

| Reviewed source | Adaptation here | Deliberately omitted |
| --- | --- | --- |
| [skills.sh catalog](https://www.skills.sh/) | Selected gaps rather than installing a whole leaderboard | Popularity as proof of quality |
| [frontend-design](https://www.skills.sh/anthropics/skills/frontend-design) | Product-specific direction in interface-craft | Mandatory novelty or a new brand for small edits |
| [web-design-guidelines](https://www.skills.sh/vercel-labs/agent-skills/web-design-guidelines) and [source](https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md) | Focused UI and accessibility evidence | Universal typography, framework, and list-size rules |
| [webapp-testing](https://www.skills.sh/anthropics/skills/webapp-testing) | Observe, interact, and verify in browser-ui-validation | Required Python/Playwright setup and universal network-idle waits |
| [agent-browser](https://www.skills.sh/vercel-labs/agent-browser/agent-browser) and [source](https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/SKILL.md) | Read installed tool documentation; keep session context | Forced CLI installation or replacing the user's browser |
| [systematic-debugging](https://www.skills.sh/obra/superpowers/systematic-debugging) | Hypothesis-driven debug-root-cause | Rigid phase and attempt counts |
| [UI Skills catalog](https://www.ui-skills.com/) and [UI Skills Root](https://www.ui-skills.com/skills/ibelick/ui-skills-root) | Choose guidance by task and actual stack | Extra routing CLI dependency or arbitrary skill-count limits |
| [Improve UI](https://www.ui-skills.com/skills/ibelick/improve-ui) | Prove design ownership and recheck findings | Planning-only execution, fixed findings count, excluding relevant accessibility defects |
| [Baseline UI](https://www.ui-skills.com/skills/ibelick/baseline-ui) | Local components, meaningful state feedback, coherent tokens | Mandatory libraries, color bans, and universal motion values |
| [Better UI](https://www.ui-skills.com/skills/jakubkrehel/better-ui) | Contextual craft and motion review | Fixed scale/easing/blur recipes and automatic approval verdicts |
| [Improve Animations](https://www.ui-skills.com/skills/emilkowalski/improve-animations) | Purpose, frequency, interruption, verification in interaction-motion | Forced delegation, refusing requested fixes, mandatory plan folders |

The UI Skills pages were read in the in-app browser. The table distinguishes
useful ideas from source-specific operating rules; loading a source for research
does not make its instructions active policy in this repository.

## Tool and standards references

- [Official Browser documentation](https://learn.chatgpt.com/docs/browser), plus
  current in-session browser API documentation, informs the optional Codex
  browser reference. Capabilities must be discovered at execution time.
- [Playwright best practices](https://playwright.dev/docs/best-practices) informs
  user-visible assertions, isolation, and semantic locators without requiring
  Playwright in other environments.
- [W3C accessibility evaluation](https://www.w3.org/WAI/test-evaluate/) and
  [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/) support targeted
  accessibility evaluation and its limits.
- [Web Vitals](https://web.dev/articles/vitals) informs the distinction between
  lab measurements and observed user performance in frontend-performance.

The existing Interfaces cheat-sheet index is retained as an optional dated
reference for explicitly requested source audits. It was not re-audited in this
update and is not required for ordinary UI work. Existing TypeScript references
remain conditional on TypeScript use. The named private-project example in the
previous monorepo reference was removed.
