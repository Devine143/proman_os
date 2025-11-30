# Architecture Principles

**Design philosophy and context management strategies**

---

## The 4L Principle

| Principle | Meaning | Application |
|-----------|---------|-------------|
| **Low Human** | AI handles operations | Automate repeatable work |
| **Low Cost** | Single tool, no complex stack | Claude Code as the engine |
| **Low Complexity** | Simple yet integrated | Components compose cleanly |
| **Low Tech** | No coding for operation | SOPs become executable skills |

**Why:** As the system scales, these constraints ensure manageability. Complexity is the enemy of delegation.

---

## Progressive Disclosure

**Problem:** Loading all context every session wastes tokens and pollutes working memory.

**Solution:** Lean hub files that point to detailed documentation.

```
CLAUDE.md (200 lines) → "For budget details, see COO/docs/..."
    ↓
COO/docs/workflow.md  → Loaded only when relevant
```

**Rule:** No CLAUDE.md file exceeds 200 lines. Details live in `/docs/` directories.

---

## Context Hygiene

**Problem:** Long sessions accumulate context that dilutes focus.

**Solution:** Active context management through pruning and summarization.

### Session Length Actions

| Duration | Action |
|----------|--------|
| < 30 min | No action needed |
| 30-60 min | Summarize completed work to WORKING.md |
| > 60 min | Prune message history; preserve only active task |

### What to Preserve vs. Summarize

| Preserve (High Signal) | Summarize (Low Signal) |
|------------------------|------------------------|
| Current task requirements | Completed task details |
| Active blockers | Resolved issues |
| Pending decisions | Made decisions (just outcomes) |
| Error context (if debugging) | Successful operations |

### WORKING.md During Extended Sessions

```markdown
## Current Session State
**Active Task:** [What you're doing now]
**Key Context:** [2-3 critical bullets]
**Decisions Made:** [Outcomes only]
**Next Steps:** [Immediate actions]

## Parked Context
[Details that might be needed but aren't active]
```

### Context Pollution Signals

Watch for:
- Repeated re-reading of same files
- Confusion about which task is active
- Conflating details from different tasks
- Slow response times

**Recovery:** Explicitly state: "Let me reset context. Current active task is [X]."

---

## YAML Headers Everywhere

**Problem:** Claude can't efficiently search/filter files without metadata.

**Solution:** Standard YAML headers on all significant files.

```yaml
---
type: [project-status | sop | template | skill | agent]
project: [Project name if applicable]
status: [active | completed | archived | draft]
priority: [high | medium | low]
last_updated: YYYY-MM-DD
owner: [Person responsible]
tags: [comma, separated, tags]
---
```

**Benefits:**
- Search by type, status, project
- Files self-document purpose
- Enables intelligent filtering

---

**Version:** 1.0
**Last Updated:** 2025-11-29
