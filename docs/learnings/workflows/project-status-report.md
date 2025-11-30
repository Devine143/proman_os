# Project Status Report Workflow
> Last updated: 2025-11-30

## Overview

Generate client-facing project status reports using COO domain tools. Reports follow PMP methodology and Proman standards.

## Trigger

- User says: "AI Project Status for [project]"
- Or: `/project-status` command

## Pre-Flight Checks

1. Verify project folder exists in `COO/projects/`
2. Check for recent updates in project files
3. Identify reporting period

## Steps

### 1. Gather Data
- Review project folder contents
- Check for:
  - Budget tracking files
  - Schedule/timeline docs
  - Recent correspondence
  - Issue logs

### 2. Analyze Status
For each knowledge area:
- **Schedule:** On track / Delayed / Ahead
- **Budget:** Under / On / Over budget
- **Scope:** Changes requested / Approved / None
- **Quality:** Issues identified / Resolved
- **Risk:** New risks / Mitigated risks

### 3. Draft Report
Standard sections:
1. Executive Summary (1 paragraph)
2. Key Accomplishments This Period
3. Upcoming Milestones
4. Issues & Risks
5. Budget Status (if applicable)
6. Next Steps

### 4. Review
- CEO reviews before client delivery
- Check for sensitive information
- Verify accuracy of dates and figures

## Output Location

Save drafts to: `COO/projects/[project-name]/reports/`

## Common Pitfalls

- Don't include internal notes in client report
- Verify all numbers before sending
- Keep executive summary to 3-4 sentences
- Always end with clear next steps

## Related

- `gotchas/client-preferences.md` - Client-specific formatting
