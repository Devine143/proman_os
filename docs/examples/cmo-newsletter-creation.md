# Example: Newsletter Creation

**Domain:** CMO
**Demonstrates:** Content workflow, draft-edit-publish cycle, platform-specific adaptation

---

## Interaction Transcript

**User:** Write a newsletter post about using AI for budget analysis

**Claude:**
*[Loads newsletter-creation skill]*
*[Reads CMO/docs/content-strategy.md for voice and pillars]*
*[Checks CMO/newsletter-archive/ for related past posts]*

Good topic - this fits the "AI Implementation" pillar and draws from real COO operations. Let me clarify the angle:

1. **Free tier (what + why):** Benefits of AI-assisted financial tracking, the problem it solves
2. **Paid tier (how):** Step-by-step implementation guide

Which tier is this for? Or both as a series?

**User:** Start with free tier

**Claude:**
*[Drafts post following free tier structure]*
*[Saves to: CMO/newsletter-drafts/ai-budget-analysis-automation-free.md]*

Draft created: `CMO/newsletter-drafts/ai-budget-analysis-automation-free.md`

**Draft Summary:**
- Hook: "I stopped manually calculating CPI/SPI. Here's what happened."
- Problem: Average PM spends 4+ hours/month on budget reconciliation
- Solution tease: AI-assisted variance analysis and reporting
- CTA: "Next week I'll show you exactly how to set this up" (paid tier tease)

**Word count:** 847 (target: 800-1000)
**Reading time:** ~4 minutes

Ready for your review. What changes would you like?

**User:** Good, but make the hook more specific

**Claude:**
*[Reads current draft]*
*[Revises hook section]*

Updated hook options:

1. "R2.3M budget. 47 line items. One AI prompt. Here's what happened."
2. "Last month I generated 12 budget reports. I calculated 2 of them manually."
3. "The cost overrun I missed for 3 weeks? AI caught it in 4 seconds. Here's the difference."

Which direction resonates?

**User:** Option 2

**Claude:**
*[Updates draft with selected hook]*
*[Saves updated version]*

Updated: `CMO/newsletter-drafts/ai-budget-analysis-automation-free.md`

The hook now leads with the concrete "12 reports, 2 manual" framing. Ready for final review before publishing, or should I also draft the LinkedIn teaser?

---

## Key Behaviors Demonstrated

1. **Strategy Alignment:** Checked content pillars and past posts
2. **Tier Clarification:** Asked about free vs. paid before drafting
3. **Structured Output:** Clear summary with word count and reading time
4. **Iterative Refinement:** Offered hook options rather than guessing
5. **Cross-Platform Awareness:** Proactively mentioned LinkedIn adaptation
6. **Draft Location:** Saved to `newsletter-drafts/` not `newsletter-archive/`

---

## Content Workflow Stages

```
Idea → Draft (drafts/) → Edit → Review → Publish (archive/)
                ↓
         LinkedIn teaser
         Substack notes
```

---

## Anti-Patterns Avoided

- Did NOT publish without CEO review
- Did NOT guess the content tier
- Did NOT provide single "take it or leave it" hook
- Did NOT save draft to archive (not published yet)
