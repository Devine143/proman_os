# Folder Structure

**Target state for PROMAN_OS organization**

---

## System Layout

```
PROMAN_OS/
├── CLAUDE.md                      # Lean hub (~150 lines)
├── content-opportunities.md       # Cross-domain feed
│
├── docs/                          # Root-level detailed docs
│   ├── architecture/              # System design (this directory)
│   ├── business-context.md        # Business model, vision, goals
│   └── troubleshooting.md         # System-wide troubleshooting
│
├── COO/                           # Operations domain
│   ├── CLAUDE.md                  # Lean hub (~140 lines)
│   ├── docs/                      # Detailed COO documentation
│   │   ├── agent-guide.md
│   │   ├── project-structure.md
│   │   └── workflow-details.md
│   ├── projects/                  # Active projects (YAML headers)
│   ├── templates/                 # Document templates
│   ├── references/                # JBCC, communication, negotiation
│   ├── sops/                      # Standard operating procedures
│   └── .claude/
│       ├── agents/                # 11 agents
│       ├── skills/                # COO-specific skills
│       ├── commands/
│       └── hooks/
│
├── CMO/                           # Content marketing domain
│   ├── CLAUDE.md                  # Lean hub (~130 lines)
│   ├── docs/                      # Detailed CMO documentation
│   │   ├── content-strategy.md
│   │   ├── publishing-workflow.md
│   │   └── performance-tracking.md
│   ├── newsletter-archive/        # Published content
│   ├── newsletter-drafts/         # Work in progress
│   ├── new-post-ideas/            # Content pipeline
│   ├── linkedin-posts/            # LinkedIn content
│   └── .claude/
│       ├── agents/                # 6 agents
│       ├── skills/
│       ├── commands/
│       └── output-styles/
│
└── .claude/                       # Root configuration
    ├── CLAUDE.md                  # Config documentation (~95 lines)
    ├── agents/                    # 5 cross-domain agents
    ├── skills/                    # Shared skills
    ├── commands/                  # CEO commands
    ├── hooks/                     # System-wide hooks
    │   └── utils/                 # Shared hook utilities
    ├── backups/                   # Auto-generated (7-day retention)
    ├── logs/                      # Operation logs
    ├── state/                     # State snapshots
    └── settings.json              # Main configuration
```

---

## Project Structure (COO)

Each project follows PMP phases:

```
projects/[project-name]/
├── 00-inbox/           # Unsorted incoming (<24h retention)
├── 01-initiation/      # Feasibility, requirements
├── 02-planning/        # Fee proposals, program, PM plan
├── 03-design/          # Design submissions
├── 04-consultants/     # Civil, electrical, structural
├── 05-procurement/     # Orders, quotations, LOIs
├── 06-compliance/      # Approvals, safety, regulations
├── 07-execution/       # Construction phase
├── 08-handover/        # Completion, snag lists
├── 09-meetings/        # Minutes and agendas
└── logs/               # Automation records
```

---

## Skill Directory Structure

```
skill-name/
├── SKILL.md        # Entry point (under 150 lines)
├── knowledge/      # Reference docs, edge cases
├── templates/      # Output templates
├── examples/       # Sample outputs
└── scripts/        # Automation code
```

---

## Agent Directory Structure (when >80 lines)

```
.claude/agents/[name]/
├── [name].md           # Core identity + routing
├── procedures.md       # Detailed workflows
├── output-formats.md   # Templates for outputs
└── examples.md         # Sample interactions
```

---

**Version:** 2.0 - Removed Working Memory & Domain Status
**Last Updated:** 2025-11-30
