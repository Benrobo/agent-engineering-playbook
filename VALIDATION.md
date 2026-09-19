# Validation

Checked 19 September 2026. The original 17 skills and the added interface-craft skill passed the skill frontmatter/scaffold validator. Every skill includes a readme and keeps its procedure self-contained. Local package Markdown links resolve.

The interface source page was read in full: 61 entries across seven sections. Its public text and accessible demo structure were inspected, with a representative nested-shape demo visually checked. This is not a claim that all interactive demos or every browser combination were tested. The package contains an original workflow and compact source index, not copies of the site's full examples or paid resources.

The installer passed seven isolated behavioral tests after this cleanup. It compares installed file hashes and does not verify runtime agent activation.

Run installer tests:

```sh
python3 -m unittest discover -s tests -v
```

Skills remain project-adaptable procedures, not validated integrations with every project. Each readme provides trial scenarios. Configure real project facts and evaluate behavior before relying on them. No private source scripts, credentials, or customer payloads are included.
