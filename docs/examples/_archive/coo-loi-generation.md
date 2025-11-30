# Example: LOI Generation

**Domain:** COO
**Demonstrates:** Skill invocation, information gathering, proper file naming, escalation awareness

---

## Interaction Transcript

**User:** Create an LOI for Cape Plumbing for the Arowana project bathroom fit-out

**Claude:**
I'll generate an LOI for Cape Plumbing. Let me gather the required information.

*[Loads loi-management skill]*
*[Reads COO/projects/arowana/02-planning/budget.csv for provisional sum]*
*[Reads COO/templates/loi-template.docx]*

Before I generate the LOI, I need to confirm:
1. **Provisional Sum:** R485,000 (from budget) - correct?
2. **Scope:** Bathroom fit-out only, or full plumbing package?
3. **Timeline:** Standard 14-day acceptance period?

**User:** Yes to provisional sum, bathroom fit-out only, and yes 14 days is fine

**Claude:**
*[Generates LOI using template]*
*[Saves to: COO/projects/arowana/05-procurement/Cape_Plumbing_LOI_20251129.docx]*

LOI created: `COO/projects/arowana/05-procurement/Cape_Plumbing_LOI_20251129.docx`

**Summary:**
- Contractor: Cape Plumbing
- Scope: Bathroom fit-out (Arowana project)
- Provisional Sum: R485,000
- Acceptance: 14 days

**Next steps:** Review the document before sending. Want me to draft a cover email?

---

## Key Behaviors Demonstrated

1. **Skill Recognition:** Recognized "LOI" trigger and loaded appropriate skill
2. **Information Gathering:** Pulled provisional sum from existing budget file
3. **Clarification Before Action:** Confirmed scope and timeline before generating
4. **Proper File Naming:** `[Company]_[Type]_[Date].ext` format
5. **Correct Filing:** Placed in `05-procurement/` folder per project structure
6. **No Automatic Sending:** Generated draft for CEO review (client-facing = escalate)
7. **Proactive Next Steps:** Offered related assistance without overstepping

---

## Anti-Patterns Avoided

- Did NOT assume scope from partial information
- Did NOT send to contractor without review
- Did NOT use generic filename like "LOI.docx"
- Did NOT place file in project root or wrong folder
