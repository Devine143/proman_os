# Example: Cross-Domain Content Flow

**Domain:** COO → CMO
**Demonstrates:** Operations-to-content flywheel, domain handoff, content opportunity capture

---

## Interaction Transcript

**User:** I just set up an automated budget variance alert system for Arowana. Log this as a content opportunity.

**Claude:**
*[Updates COO/projects/arowana/PROJECT_STATUS.md with implementation note]*
*[Reads content-opportunities.md]*
*[Appends new opportunity]*

Logged to `content-opportunities.md`:

```markdown
## Budget Variance Alerts (Logged: 2025-11-29)

**Source:** Arowana project COO implementation
**Type:** AI Workflow
**Pillar:** AI Implementation

**What was built:**
- Automated monitoring of budget line items
- Threshold-based alerts (>5% variance triggers notification)
- Connected to project cost tracking CSV

**Content angles:**
- Free: Why real-time budget visibility prevents project overruns
- Paid: Step-by-step guide to building variance alerts with Claude

**Status:** Ready for CMO review
```

This fits the flywheel pattern well - real operational learning → authority-building content.

Want me to start a CMO draft now, or queue it for your next content session?

**User:** Start the free tier outline

**Claude:**
Switching to CMO domain.

*[Loads CMO/CLAUDE.md for context]*
*[Loads newsletter-creation skill]*

**Draft outline** for free tier post:

**Working title:** "The $47,000 Mistake I Almost Made (And How AI Caught It First)"

**Structure:**
1. **Hook:** Near-miss story from Arowana (anonymized)
2. **Problem:** Budget spreadsheets get stale; variance compounds silently
3. **Insight:** AI can watch what humans forget to check
4. **Tease:** "Next week: exactly how I built this in 30 minutes"

**Estimated length:** 900 words

Saved outline to: `CMO/newsletter-drafts/budget-variance-alerts-outline.md`

Ready to develop into full draft, or want to refine the angle first?

---

## Key Behaviors Demonstrated

1. **Dual Update:** Updated both COO project status AND content opportunities
2. **Structured Capture:** Used consistent format for content opportunity
3. **Content Angles:** Identified both free and paid tier potential
4. **Explicit Domain Switch:** Announced transition from COO to CMO
5. **Context Reload:** Loaded CMO CLAUDE.md when switching domains
6. **Flywheel Awareness:** Explicitly connected to operations → content pattern

---

## Cross-Domain Handoff Protocol

```
COO Work Complete
       ↓
Log to content-opportunities.md (with structured format)
       ↓
Explicit domain switch announcement
       ↓
Load CMO context (CLAUDE.md, skill)
       ↓
CMO content development
```

---

## Anti-Patterns Avoided

- Did NOT skip the content opportunity logging
- Did NOT blend COO and CMO work without explicit switch
- Did NOT forget to reload domain context
- Did NOT reveal client-identifying details in content angle
