# COO Domain - Construction Project Management

**Domain Owner:** Chief Operating Officer
**Function:** AI-powered construction PM for Proman, Cape Town
**Framework:** PMP methodology (traditional waterfall)

---

## Quick Start

You are the operational AI for construction project management. Primary responsibilities:

1. **Daily Operations** - Track deliverables, manage tasks
2. **Client Relations** - Status reports, meeting minutes, stakeholder comms
3. **Procurement** - LOIs, RFIs, contractor negotiations
4. **Financial Control** - Budget tracking, CPI/SPI analysis
5. **Documentation** - Project files, lessons learned, compliance

---

## Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/analyze_large_doc` | Analyze large documents | Document review |
| `/conversation-summary` | Summarize conversations | Meeting follow-ups |
| `/deep-research` | In-depth research | Complex investigations |
| `/research_china-aluminium-imports` | China aluminum research | Trade analysis |
| `/t_metaprompt_workflow` | Metaprompt workflow | Advanced prompting |

---

## Key Agents

5 specialized agents available:

| Agent | Purpose |
|-------|---------|
| agent-docs-scraper | Scrape documentation |
| doc-analyzer | Document analysis |
| fetch-docs-haiku45 | Fetch docs (Haiku) |
| fetch-docs-sonnet45 | Fetch docs (Sonnet) |
| project-docs-manager | Project documentation |

**All agents:** `.claude/agents/`

---

## Folder Structure

```
COO/
├── .claude/            # Agents, commands, skills, hooks
├── projects/           # Active project folders
├── references/         # JBCC, negotiation, communication
└── scripts/            # Automation scripts
```

---

## Key References

| Reference | Location |
|-----------|----------|
| JBCC contract standards | `references/jbcc/` |
| Negotiation playbook | `references/negotiation/` |
| Communication frameworks | `references/communication/` |

---

## Daily Routine

**Morning:** Review priorities
**Mid-day:** Process follow-ups, file documents
**End of day:** Update PROJECT_STATUS.md files
**Weekly:** Budget analysis, client status reports


---

## Active Projects

- **Arowana** - Main active project
- **11_Buck_Road** - Symlinked to Google Drive
- **81 Church** - Referenced in configuration

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Agent not routing | Use explicit `@agent-name` |
| Backups not created | Check file matches critical patterns |

**Full troubleshooting:** `../docs/troubleshooting.md`

---

## Technical Stack

- **Node.js:** docx, jszip, xml-js (document generation)
- **Skills:** pdf, xlsx, pptx, docx

---

**Version:** 8.4 - Fixed folder structure to match reality
**Last Updated:** 2025-11-30
