# Validation

Checked 29 September 2026 after updating all 19 existing skills and adding six,
for a total of 25. The changes are Markdown guidance and references; installer
implementation and tests were not changed.

## Executed checks

- All 25 skills passed the skill-creator frontmatter/scaffold validator. Its
  PyYAML dependency was supplied through a temporary uv environment, without
  adding a project or global dependency.
- All nine installer behavioral tests passed.
- Installed all 25 packages into both agent discovery directories in a temporary
  project and compared complete source/destination manifests: all 50 copies
  matched, including supporting references. The temporary project was removed.
- Local Markdown link targets resolved. Git whitespace checks passed.
- Reviewed descriptions, conditional references, and task boundaries. Removed
  the named private-project example and searched distributable skills for the
  source project's identifiers, local user paths, and disabled implicit invocation.

Reproduce the existing installer tests without rewriting tracked bytecode:

```sh
python3 -B -m unittest discover -s tests -v
```

## Research and judgment review

Read the user-supplied architecture skill and formatting reference. Reviewed the
selected skills.sh listings and primary references described in [SOURCES.md](SOURCES.md).
Read UI Skills Root, Improve UI, Baseline UI, Better UI, and Improve Animations
in the in-app browser. The resulting skills adapt the reasoning without importing
required libraries, fixed visual recipes, forced delegation, or planning-only
restrictions.

Reviewed the written workflows against different task conditions: a small CLI
project, existing web components, native UI without native testing access,
continuous network activity, an unavailable authenticated browser session,
and a review-only request. These were instruction walkthroughs, not executed
application tests or independent-agent evaluations. New skill readmes include
concrete trial scenarios and expected behavior for future evaluation.

## Limits

Packaging, copying, and links are verified. Automatic runtime skill selection
and engineering outcomes across arbitrary codebases are not verified. No new
skills were installed globally or into the source application. Source URLs can
change; active browser documentation remains authoritative for tool use.

The optional Interfaces cheat-sheet index retains its earlier dated research:
61 entries across seven sections, originally inspected 18 September 2026. This
update did not re-audit those demonstrations. It is not required for ordinary UI
work, and neither that review nor these checks establish accessibility certification.
