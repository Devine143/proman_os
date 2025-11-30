# Data Flows

**How information moves through PROMAN_OS**

---

## Skill Invocation Flow

```
User: "Create a budget spreadsheet"
              ↓
Claude recognizes spreadsheet → matches xlsx skill
              ↓
Skill loads: SKILL.md instructions
              ↓
Claude follows workflow, uses openpyxl/pandas
              ↓
Script executes: creates .xlsx with formulas
              ↓
Output: Professional, formatted spreadsheet
```

---

## Power Combo Flow (Agent + Skill)

```
User: "Handle procurement for the electrical package"
              ↓
Task routes to: procurement-manager agent
              ↓
Agent has skills: [docx, pdf, xlsx]
              ↓
Agent assesses situation, invokes relevant skill
              ↓
Skill provides process; Agent applies judgment
              ↓
Output: Complete procurement package
```

---

## Cross-Domain Flow (Operations → Content)

```
COO: Implements new AI workflow for budget analysis
              ↓
Hook/Agent detects: "This could be content"
              ↓
Logged to: content-opportunities.md
              ↓
CMO: Reviews opportunities, drafts newsletter post
              ↓
Published: Newsletter builds authority
              ↓
Result: New client inquiries → more operations
```

**The Flywheel:**
```
COO Operations  →  Document learnings  →  content-opportunities.md
        ↑                                          ↓
Authority attracts clients              CMO creates content
        ↑                                          ↓
        ←←←←←←  Content builds authority  ←←←←←←←←
```

---

## CEO Reporting Flow

**Daily:**
```
/daily-briefing → Reads COO/DOMAIN-STATUS.md + CMO/DOMAIN-STATUS.md
              → Aggregates into quick health check
              → Terminal output
```

**Weekly:**
```
/weekly-review → Deep analysis of both domains
              → Generates comprehensive report
              → Saves to weekly-reviews/
```

---

## Session Lifecycle Flow

```
Session Start → session_start.py hook
                    ↓
              Check WORKING.md files
                    ↓
              Display CEO dashboard
                    ↓
Work happens → pre_tool_use.py (backup before edits)
            → post_tool_use.py (log operations)
                    ↓
Session End → session_end.py (cleanup)
```

---

## Context Loading Strategy

**Session Start:**
```
Load: CLAUDE.md + WORKING.md
Check: Which domain? → Load domain CLAUDE.md + DOMAIN-STATUS.md
Total: ~5,300 tokens (baseline)
```

**Task Execution:**
```
Identify skill/agent → Load SKILL.md (~600 tokens)
If edge case → Load knowledge/ excerpts (~500-1000)
Generate output → Load template
Total per task: ~1,500-2,500 additional tokens
```

**Deep Analysis:**
```
Load project docs selectively
Use excerpts, not entire files
Summarize as you go
Budget: ~5,000 tokens for analysis context
```

---

**Version:** 1.0
**Last Updated:** 2025-11-29
