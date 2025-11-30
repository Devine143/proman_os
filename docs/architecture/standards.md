# Standards

**Naming conventions, status indicators, and backup strategy**

---

## File Naming

### COO Domain
```
[Company_Name]_[Document_Type]_[Date_YYYYMMDD].[ext]
```
Example: `ABC_Plumbing_LOI_20251129.docx`

### CMO Domain
```
Descriptive hyphenated names
```
Example: `ai-budget-analysis-automation.md`

---

## Status Indicators

| Status | COO Meaning | CMO Meaning |
|--------|-------------|-------------|
| Green | <5 overdue, no blockers | Engagement >=3.5%, on schedule |
| Yellow | 5-10 overdue OR decisions pending >7d | Engagement 2-3.5% OR behind |
| Red | >10 overdue OR critical path blocked | Engagement <2% OR no pipeline |

---

## Backup Strategy

### What Gets Backed Up
- `projects/*/05-procurement/*` (LOIs, quotes)
- `projects/*/02-planning/*` (budgets, schedules)
- `*_budget*`, `*_cost_model*`, `*_risk_register*`
- `PROJECT_STATUS.md`

### Location
`.claude/backups/YYYY-MM-DD/`

### Retention
7 days

---

## Integration Points

| System | Purpose | Domain |
|--------|---------|--------|
| Google Drive | Project file storage via symlinks | COO |
| Substack | Newsletter publishing, analytics | CMO |
| Autodesk Construction Cloud | Project knowledge hub (future) | COO |

---

## Version Control

- COO and CMO have separate Git repositories
- Root is not a Git repo (subdomains independent)
- Commit style: Human-style, no AI attribution

---

## Scaling Considerations

When PROMAN_OS grows:

1. **New Team Members:** Read architecture/index.md first
2. **New Skills:** Follow skill directory structure
3. **New Agents:** Create with complete YAML header
4. **New Domains:** Replicate COO/CMO structure
5. **Cross-Domain Work:** Use root-level files

**Always ask:** Does this follow the 4L Principle?

---

**Version:** 1.1 - Removed DOMAIN-STATUS.md reference
**Last Updated:** 2025-11-30
