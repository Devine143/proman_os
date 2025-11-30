# COO Domain - Construction Project Management

**Domain Owner:** Chief Operating Officer
**Function:** AI-powered construction PM for Proman, Cape Town
**Framework:** PMP methodology (traditional waterfall)

---

## Environment

You are working in Mac OS, running on Apple Silicon (M4 Max).

- Use the `uv` tool for all Python project and dependency management, and also for running Python (there is no Python directly installed)
- Use `uvx` to run Python-based CLI tools without installing them (e.g., `uvx yt-dlp`, `uvx ruff`, etc.). Never use `uv tool install` unless explicitly needed
- Since you are on a Mac, you can use AppleScript (`osascript`) to automate various things in the OS and apps

### Usage Notes

You are a general purpose assistant, not limited to coding. Can write code to help with various tasks.

### Git Commit Guidelines

When making git commits, do NOT include the "Generated with [Claude Code]" line or "Co-Authored-By: Claude" attribution in commit messages. Write commit messages as if they were written directly by me, using a clean, professional format.

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

## Main Execution Loop (CRITICAL — FOLLOW EVERY TIME)

When given ANY task, you MUST follow this loop:

### Step 1: STOP AND SEARCH MEMORIES (MANDATORY)

Before doing ANYTHING else:

- Search `docs/learnings/` for relevant workflows
- Check `docs/learnings/README.md` to see all available workflows
- Use grep for specific topics in `docs/learnings/`
- READ any potentially relevant workflow files completely

### Step 2: DECISION POINT

- If a workflow exists → USE IT EXACTLY AS WRITTEN
- If no workflow exists → Plan your approach and document why no existing workflow applies

### Step 3: EXECUTE

- Follow the existing workflow step-by-step, OR
- Execute your new approach

### Step 4: CAPTURE LEARNING

- If you created a new workflow → Save it to `docs/learnings/workflows/`
- If you found issues with an existing workflow → Update it
- Update the index at `docs/learnings/README.md`

### VIOLATIONS TO AVOID

- ❌ NEVER skip memory check because you think you know what to do
- ❌ NEVER create your own approach when a workflow exists
- ❌ NEVER assume a simple task doesn't have a workflow
- ❌ NEVER proceed without explicitly stating whether you found a relevant workflow

### Example Execution

User: "Create a newsletter post"

✅ CORRECT:
Check memories → Find `docs/learnings/workflows/newsletter-creation.md` → Follow it

❌ WRONG:
Jump straight to drafting without checking existing workflow

---

## Instructions & Projects

- Search `docs/learnings/` to see if there's relevant information for queries, especially if missing context
- For multi-session work, update the relevant `WORKING.md` file (root, `COO/WORKING.md`, or `CMO/WORKING.md`)
- Skip WORKING.md updates for one-off tasks

### Automatic Workflow Memory Capture

IMPORTANT: After completing ANY multi-step workflow or discovering new system behavior:

1. Automatically create a memory in `docs/learnings/workflows/[workflow-name].md`
2. Update the index at `docs/learnings/README.md`
3. Follow the format template in the README

This should happen WITHOUT being asked — recognize when you've learned something worth persisting.

---

## Memory Reference

| Type | Location | When to Check |
|------|----------|---------------|
| Workflows | `docs/learnings/workflows/` | "How do we do X?" |
| Decisions | `docs/learnings/decisions/` | "Why did we choose X?" |
| Gotchas | `docs/learnings/gotchas/` | Errors or confusion |

---

**Version:** 8.6 - Added Environment section (uv, uvx, AppleScript, git guidelines)
**Last Updated:** 2025-11-30
