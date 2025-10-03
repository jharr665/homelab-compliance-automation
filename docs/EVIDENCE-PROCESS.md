# EVIDENCE-PROCESS

- **Raw scanner outputs** → `compliance-automation/reports/json/`
- **Markdown summaries** → `compliance-automation/evidence-store/obsidian/`
- **PDF reports** → `compliance-automation/reports/pdf/`
- **Tamper evidence** → Git commit history; optional Rekor entry

Automation:
- Weekly CI runs scans (or triggers cluster CronJobs) and commits JSON results.
- `exporters/json_to_md.py` appends Obsidian-ready summaries with timestamps and control IDs.
