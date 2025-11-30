# Edge Case: Multi-Domain Task

**Demonstrates:** Domain handoff protocol, context management across domains

---

## Scenario: Task Spans Both Domains

**User:** Document the new procurement workflow I built and turn it into a newsletter post

**Claude:**
This task spans both domains. I'll handle it in sequence:

1. **COO:** Document the procurement workflow (operational record)
2. **CMO:** Create newsletter content from the documentation

Starting with COO documentation.

---

### Phase 1: COO Documentation

*[Loads COO/CLAUDE.md]*
*[Reads current procurement process files]*

**Questions for documentation:**

1. What triggers this workflow? (e.g., "new contractor needed")
2. What tools/skills are involved?
3. What's the output/deliverable?

**User:** It triggers when we need to onboard a new contractor. Uses the procurement-manager agent with LOI and negotiation skills. Outputs signed LOI and contractor added to project register.

**Claude:**
*[Creates documentation]*
*[Saves to COO/docs/workflow-details.md - appended]*

Documented in COO. Key additions:
- New section: "Contractor Onboarding Workflow"
- Trigger, process steps, tools, outputs captured
- Cross-referenced with relevant SOPs

**COO portion complete. Switching to CMO domain.**

---

### Phase 2: CMO Content Development

*[Loads CMO/CLAUDE.md]*
*[Loads newsletter-creation skill]*
*[References the COO documentation just created]*

For the newsletter, I need to clarify the angle:

1. **Free tier:** "Why AI-assisted procurement saves 5 hours per contractor" (benefits focus)
2. **Paid tier:** "Build your own contractor onboarding workflow" (implementation guide)
3. **Both:** Free teases, paid delivers

Which approach?

**User:** Both - make it a two-part series

**Claude:**
*[Creates content plan]*
*[Drafts free tier outline]*
*[Saves to CMO/newsletter-drafts/procurement-workflow-series/]*

Created series structure:

```
CMO/newsletter-drafts/procurement-workflow-series/
├── series-plan.md           # Overall series strategy
├── part-1-free-draft.md     # Benefits/why (free tier)
└── part-2-paid-outline.md   # How-to guide (paid tier)
```

**Part 1 (Free) - Ready for review:**
- Hook: "Last month I onboarded 4 contractors in 3 hours. Here's the shift."
- Focus: Time savings, consistency, reduced errors
- CTA: Teases Part 2 how-to

**Part 2 (Paid) - Outlined:**
- Full implementation walkthrough
- References COO documentation for accuracy
- Includes template downloads

Ready to develop Part 1 draft, or adjust the series plan?

---

## Key Behaviors Demonstrated

1. **Explicit Sequencing:** Announced two-phase approach upfront
2. **Domain Isolation:** Completed COO fully before switching
3. **Context Reload:** Loaded CMO CLAUDE.md at domain switch
4. **Cross-Reference:** CMO content references COO documentation
5. **Clean Handoff:** Clear "switching to CMO" announcement
6. **No Context Bleed:** Didn't mix operational details into content draft

---

## Multi-Domain Handoff Protocol

```
Identify multi-domain task
       ↓
Announce sequence to user
       ↓
Complete Domain 1 fully
  - Load domain context
  - Execute work
  - Save outputs
  - Announce completion
       ↓
Explicit switch announcement
       ↓
Complete Domain 2
  - Load domain context (fresh)
  - Reference Domain 1 outputs as needed
  - Execute work
       ↓
Summarize cross-domain outcomes
```

---

## Anti-Patterns Avoided

- Did NOT try to do both domains simultaneously
- Did NOT skip the explicit domain switch
- Did NOT carry COO context into CMO work (reloaded fresh)
- Did NOT mix operational details into content draft
