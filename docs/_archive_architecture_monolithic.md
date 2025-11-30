# PROMAN_OS System Architecture

**Source of Truth for System Design and Philosophy**

**Last Updated:** 2025-11-29

---

## Core Philosophy: The 4L Principle

Every architectural decision in PROMAN_OS follows four constraints:

| Principle | Meaning | Application |
|-----------|---------|-------------|
| **Low Human** | AI handles operations | Minimize manual intervention; automate repeatable work |
| **Low Cost** | Single tool, no complex stack | Claude Code as the engine; avoid tool sprawl |
| **Low Complexity** | Simple yet integrated | Components compose cleanly; avoid over-engineering |
| **Low Tech** | No coding required for operation | SOPs become executable skills; operators don't need to code |

**Why This Matters:** As the system scales (more projects, more team members), these constraints ensure it remains manageable. Complexity is the enemy of delegation.

---

## Architecture Principles

### 1. Progressive Disclosure

**Problem:** Loading all context every session wastes tokens and pollutes Claude's working memory.

**Solution:** Lean hub files that point to detailed documentation. Claude navigates to what it needs.

```
CLAUDE.md (200 lines)     →  "For budget details, see COO/docs/..."
    ↓
COO/docs/workflow.md      →  Loaded only when relevant
```

**Rule:** No CLAUDE.md file exceeds 200 lines. Details live in `/docs/` directories.

---

### 2. Context Hygiene

**Problem:** Long sessions accumulate context that dilutes focus and wastes tokens.

**Solution:** Active context management through pruning, summarization, and state offloading.

#### Intra-Session Management

| Session Length | Action |
|----------------|--------|
| < 30 minutes | No action needed |
| 30-60 minutes | Summarize completed work to WORKING.md |
| > 60 minutes | Prune message history; preserve only active task context |

#### What to Preserve vs. Summarize

| Preserve (High Signal) | Summarize (Low Signal) |
|------------------------|------------------------|
| Current task requirements | Completed task details |
| Active blockers | Resolved issues |
| Pending decisions | Made decisions (just outcomes) |
| Error context (if debugging) | Successful operations |

#### WORKING.md Hygiene

**During extended sessions:**
```markdown
## Current Session State
**Active Task:** [What you're doing now]
**Key Context:** [2-3 bullet points of critical info]
**Decisions Made:** [Outcomes only, not deliberation]
**Next Steps:** [Immediate actions]

## Parked Context
[Details that might be needed but aren't active]
```

**After session:**
- Clear "Current Session State"
- Move relevant outcomes to DOMAIN-STATUS.md
- Delete "Parked Context" if no longer relevant

#### Context Pollution Signals

Watch for these symptoms:
- Repeated re-reading of same files
- Confusion about which project/task is active
- Conflating details from different tasks
- Slow response times (token budget pressure)

**Recovery:** When pollution detected, explicitly state: "Let me reset context. Current active task is [X]. Clearing other context."

---

### 3. Skills: Executable SOPs

**Problem:** SOPs as flat markdown are passive—Claude reads them but can't execute deterministically.

**Solution:** Skills package knowledge + templates + scripts into executable units.

**Skill Directory Structure:**
```
skill-name/
├── SKILL.md              # YAML header + process overview
├── knowledge/            # Reference docs, examples, edge cases
├── templates/            # Output templates (docx, md, xlsx)
└── scripts/              # Deterministic code (generate docs, calculate metrics)
```

**YAML Header (enables auto-invocation):**
```yaml
---
name: loi-management
description: Generate Letters of Intent. Auto-invoke when user mentions
  LOI, letter of intent, contractor appointment, provisional sum.
tools:
  - Read
  - Write
  - Bash
---
```

**How Auto-Invocation Works:**
1. User says "Create an LOI for the plumber"
2. Claude recognizes "LOI" matches skill description
3. Skill loads → provides process, templates, scripts
4. Output is consistent and deterministic

---

### 3. The Power Combo: Agents + Skills

**Problem:** Agents are smart but lack formalized processes. Skills have processes but lack judgment.

**Solution:** Equip agents with skills. The agent provides judgment; the skill provides the playbook.

**Agent YAML Header with Skills:**
```yaml
---
name: procurement-manager
description: Handles contractor procurement, LOIs, quotes, negotiations
tools:
  - Read
  - Write
  - Bash
  - Task
skills:
  - loi-management
  - contractor-negotiation
model: sonnet
---
```

**Execution Flow:**
```
User Request → Agent receives task
                    ↓
              Agent recognizes skill is relevant
                    ↓
              Agent invokes skill
                    ↓
              Skill provides: process + templates + scripts
                    ↓
              Agent executes with judgment
                    ↓
              Consistent, high-quality output
```

---

### 4. YAML Headers Everywhere

**Problem:** Claude can't efficiently search/filter files without metadata.

**Solution:** Standard YAML headers on all significant files.

**Standard Fields:**
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
- Claude can search by type, status, project
- Files self-document their purpose
- Enables intelligent filtering and routing

---

### 5. Command Center: Daily Operational Lifeline

**Problem:** No persistent orientation across sessions.

**Solution:** Living `daily-roadmap.md` that generates at session start and updates throughout the day.

**Contents:**
- One Thing: Primary focus for today
- Department Status: COO and CMO health at a glance
- Priority Stack: Ordered task list
- Blocked: Items needing attention
- Completed: Running log of finished work

**Session Flow:**
```
Session Start → Check/generate daily-roadmap.md
                    ↓
              Display current state
                    ↓
Work happens → Post-tool hooks update roadmap
                    ↓
Session End → Roadmap reflects day's progress
```

---

### 6. Cross-Domain Intelligence: The Flywheel

**Problem:** Operations learnings don't automatically become content.

**Solution:** `content-opportunities.md` as cross-domain feed.

**The Flywheel:**
```
COO Operations     →  Document learnings  →  content-opportunities.md
        ↑                                            ↓
Authority attracts clients              CMO creates content
        ↑                                            ↓
        ←←←←←←  Content builds authority  ←←←←←←←←←←
```

**Capture Mechanism:**
- Manual: `/log-content-opportunity` command
- Automatic: Hook detects interesting operations
- Agent-based: Operations-manager identifies content-worthy work

---

## System Components

### Component Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│                        PROMAN_OS                            │
├─────────────────────────────────────────────────────────────┤
│  CLAUDE.md (Lean Hub)                                       │
│  ├── Points to: docs/, COO/, CMO/                          │
│  └── Provides: Quick reference, business context           │
├─────────────────────────────────────────────────────────────┤
│  daily-roadmap.md          │  content-opportunities.md     │
│  (Operational lifeline)    │  (Cross-domain feed)          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   COO Domain                    CMO Domain                  │
│   ┌─────────────────────┐      ┌─────────────────────┐     │
│   │ CLAUDE.md (Lean)    │      │ CLAUDE.md (Lean)    │     │
│   │ DOMAIN-STATUS.md    │      │ DOMAIN-STATUS.md    │     │
│   │ docs/               │      │ docs/               │     │
│   │ projects/           │      │ newsletter-archive/ │     │
│   │ .claude/            │      │ .claude/            │     │
│   │   ├── agents/       │      │   ├── agents/       │     │
│   │   ├── skills/       │      │   ├── skills/       │     │
│   │   ├── commands/     │      │   ├── commands/     │     │
│   │   └── hooks/        │      │   └── hooks/        │     │
│   └─────────────────────┘      └─────────────────────┘     │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  .claude/ (Root Configuration)                              │
│  ├── agents/     (Cross-domain agents)                     │
│  ├── skills/     (Shared skills)                           │
│  ├── commands/   (CEO commands)                            │
│  ├── hooks/      (System-wide automation)                  │
│  └── settings.json                                         │
└─────────────────────────────────────────────────────────────┘
```

---

### CLAUDE.md Files: Lean Hubs

| File | Target Lines | Purpose |
|------|--------------|---------|
| `/CLAUDE.md` | ~200 | Root system prompt; business context; navigation |
| `/COO/CLAUDE.md` | ~150 | Operations domain; agent/command overview |
| `/CMO/CLAUDE.md` | ~150 | Content domain; publishing workflow |
| `/.claude/CLAUDE.md` | ~100 | Configuration documentation |

**What Goes IN CLAUDE.md:**
- Quick reference tables
- Navigation pointers ("For X, see Y")
- Key triggers and commands
- Business context summary

**What Goes in `/docs/`:**
- Detailed workflows
- Reference materials
- Troubleshooting guides
- Extended documentation

---

### Skills

**Location by Scope:**
```
/.claude/skills/           # Shared across domains
/COO/.claude/skills/       # Operations-specific
/CMO/.claude/skills/       # Content-specific
```

**Key Skills (Target State):**

| Skill | Domain | Purpose |
|-------|--------|---------|
| loi-management | COO | JBCC-compliant Letters of Intent |
| budget-analysis | COO | CPI/SPI calculations, variance reports |
| contractor-negotiation | COO | Negotiation prep and playbooks |
| newsletter-creation | CMO | Draft → edit → publish workflow |
| linkedin-optimization | CMO | Hook writing, CTA optimization |
| communication-frameworks | Shared | SCQA, Pyramid Principle, MECE |
| document-formatter | Shared | Consistent output formatting |

---

### Agents

**Characteristics:**
- Specialized expertise (one job, done well)
- Context isolation (don't pollute main conversation)
- Equipped with relevant skills
- YAML headers define capabilities

**Agent Distribution:**

| Location | Count | Examples |
|----------|-------|----------|
| Root `.claude/agents/` | 6 | ceo-briefing, workflow-optimizer |
| COO `.claude/agents/` | 11 | procurement-manager, financial-controller |
| CMO `.claude/agents/` | 6 | linkedin-post-expander, newsletter-analyst |

---

### Commands

**Trigger Pattern:** `/command-name`

**Types:**
- **CEO Commands:** Strategic oversight (`/daily-briefing`, `/weekly-review`)
- **COO Commands:** Operational execution (`/loi`, `/budget-analysis`)
- **CMO Commands:** Content creation (`/newsletter-post`, `/newsletter-to-linkedin`)

---

### Hooks

**Event-Triggered Automation:**

| Hook | Trigger | Purpose |
|------|---------|---------|
| SessionStart | Session begins | Check WORKING.md, display dashboard |
| PreToolUse | Before Write/Edit | Backup critical files |
| PostToolUse | After any tool | Log operations |
| SubagentStop | Agent completes | Track performance |
| Stop | Session closes | Archive logs, clean temp files |
| PreCompact | Before compression | Save state for recovery |

#### Configuration Location

Hooks are configured in `settings.json` files:

| Scope | File |
|-------|------|
| Root (CEO) | `/.claude/settings.json` |
| COO Domain | `/COO/.claude/settings.json` |
| CMO Domain | `/CMO/.claude/settings.json` |

**Important:** Claude Code does NOT inherit settings from parent directories. Each domain needs its own `settings.json` if started as a separate session.

#### Hook Technology Standard: Python + uv

All hooks use Python with uv for consistency and power:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["python-dotenv"]
# ///
```

**Why Python/uv over Bash:**
- Complex logic handled naturally (vs awk/sed/grep chains)
- Robust error handling with try/except
- Native JSON parsing (hooks receive JSON input)
- Inline dependency declaration (no venv management)
- Easier to maintain and extend

**Hook Script Template:**
```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import json
import sys
from pathlib import Path

def main():
    try:
        input_data = json.loads(sys.stdin.read())
        # Hook logic here
        sys.exit(0)
    except Exception:
        sys.exit(0)  # Fail silently to not block Claude

if __name__ == '__main__':
    main()
```

**Shared Utilities:** Common functions live in `/.claude/hooks/utils/` and are imported by domain hooks.

#### Working Memory Integration

The SessionStart hook enforces the Working Memory Protocol:

1. Scans all WORKING.md files (root, COO, CMO)
2. Detects active tasks (ignores template placeholders)
3. Displays "RESUME PREVIOUS WORK" alert if tasks found
4. Shows dashboard with quick actions

**Implementation:** `check_working_memory()` function in `session_start.py`

#### Adding Hooks to New Domains

When creating a new domain:

1. Create `.claude/hooks/` directory in the domain
2. Copy hook templates from COO or root
3. Configure `settings.json`:

```json
{
  "hooks": {
    "SessionStart": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "uv run $CLAUDE_PROJECT_DIR/.claude/hooks/session_start.py"
      }]
    }],
    "PreToolUse": [{
      "matcher": "Write|Edit|MultiEdit",
      "hooks": [{
        "type": "command",
        "command": "uv run $CLAUDE_PROJECT_DIR/.claude/hooks/pre_tool_use.py"
      }]
    }]
  }
}
```

**Key hooks to implement:**
- `session_start.py` - Check WORKING.md, display dashboard
- `pre_tool_use.py` - Backup critical files before edits
- `pre_compact.py` - Save state before context compression

---

## Folder Structure (Target State)

```
PROMAN_OS/
├── CLAUDE.md                      # Lean hub (~200 lines)
├── daily-roadmap.md               # Living daily document
├── content-opportunities.md       # Cross-domain feed
│
├── docs/                          # Root-level detailed docs
│   ├── architecture.md            # THIS FILE (source of truth)
│   ├── business-context.md        # Business model, vision, goals
│   └── troubleshooting.md         # System-wide troubleshooting
│
├── COO/                           # Operations domain
│   ├── CLAUDE.md                  # Lean hub (~150 lines)
│   ├── DOMAIN-STATUS.md           # Current operational state
│   ├── docs/                      # Detailed COO documentation
│   │   ├── agent-guide.md
│   │   ├── project-structure.md
│   │   └── workflow-details.md
│   ├── projects/                  # Active projects (YAML headers)
│   ├── templates/                 # Document templates (YAML headers)
│   ├── references/                # JBCC, communication, negotiation
│   └── .claude/
│       ├── agents/                # 11 agents (with skills field)
│       ├── skills/                # Converted SOPs
│       │   ├── loi-management/
│       │   ├── budget-analysis/
│       │   └── contractor-negotiation/
│       ├── commands/
│       └── hooks/
│
├── CMO/                           # Content marketing domain
│   ├── CLAUDE.md                  # Lean hub (~150 lines)
│   ├── DOMAIN-STATUS.md           # Current content state
│   ├── docs/                      # Detailed CMO documentation
│   │   ├── content-strategy.md
│   │   ├── publishing-workflow.md
│   │   └── performance-tracking.md
│   ├── newsletter-archive/        # Published content
│   ├── newsletter-drafts/         # Work in progress
│   ├── new-post-ideas/            # Content pipeline
│   ├── linkedin-posts/            # LinkedIn content
│   └── .claude/
│       ├── agents/                # 6 agents (with skills field)
│       ├── skills/
│       │   ├── newsletter-creation/
│       │   └── linkedin-optimization/
│       ├── commands/
│       └── output-styles/
│
└── .claude/                       # Root configuration
    ├── CLAUDE.md                  # Config documentation (~100 lines)
    ├── agents/                    # 6 cross-domain agents
    ├── skills/                    # Shared skills
    │   ├── communication-frameworks/
    │   ├── document-formatter/
    │   └── file-organization/
    ├── commands/                  # CEO commands
    ├── hooks/                     # System-wide hooks
    ├── backups/                   # Auto-generated (7-day retention)
    ├── logs/                      # Operation logs
    ├── state/                     # State snapshots
    └── settings.json              # Main configuration
```

---

## Data Flows

### Skill Invocation Flow

```
User: "Create an LOI for ABC Plumbing"
              ↓
Claude recognizes "LOI" → matches loi-management skill
              ↓
Skill loads: SKILL.md + knowledge/ + templates/
              ↓
Claude follows process, uses template
              ↓
Script executes: generate-loi.js creates .docx
              ↓
Output: Professional, consistent LOI document
```

### Power Combo Flow (Agent + Skill)

```
User: "Handle procurement for the electrical package"
              ↓
Task routes to: procurement-manager agent
              ↓
Agent has skills: [loi-management, contractor-negotiation]
              ↓
Agent assesses situation, invokes relevant skill
              ↓
Skill provides process; Agent applies judgment
              ↓
Output: Complete procurement package
```

### Cross-Domain Flow (Operations → Content)

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

### CEO Reporting Flow

```
Daily:
/daily-briefing → Reads COO/DOMAIN-STATUS.md + CMO/DOMAIN-STATUS.md
              → Aggregates into quick health check
              → Terminal output

Weekly:
/weekly-review → Deep analysis of both domains
              → Generates comprehensive report
              → Saves to weekly-reviews/
```

---

## Standards

### File Naming

**COO Domain:**
```
[Company_Name]_[Document_Type]_[Date_YYYYMMDD].[ext]
Example: ABC_Plumbing_LOI_20251129.docx
```

**CMO Domain:**
```
Descriptive hyphenated names
Example: ai-budget-analysis-automation.md
```

### Status Indicators

| Status | COO Meaning | CMO Meaning |
|--------|-------------|-------------|
| 🟢 | <5 overdue, no blockers | Engagement ≥3.5%, on schedule |
| 🟡 | 5-10 overdue OR decisions pending >7d | Engagement 2-3.5% OR behind |
| 🔴 | >10 overdue OR critical path blocked | Engagement <2% OR no pipeline |

### Backup Strategy

**What Gets Backed Up:**
- `projects/*/05-procurement/*` (LOIs, quotes)
- `projects/*/02-planning/*` (budgets, schedules)
- `*_budget*`, `*_cost_model*`, `*_risk_register*`
- `DOMAIN-STATUS.md`, `PROJECT_STATUS.md`

**Location:** `.claude/backups/YYYY-MM-DD/`
**Retention:** 7 days

---

## Integration Points

| System | Purpose | Domain |
|--------|---------|--------|
| Google Drive | Project file storage via symlinks | COO |
| Substack | Newsletter publishing, analytics | CMO |
| Autodesk Construction Cloud | Project knowledge hub (future) | COO |

---

## Version Control

- COO and CMO have separate Git repositories
- Root is not a Git repo (subdomains independent)
- Commit style: Human-style, no AI attribution

---

## Scaling Considerations

As PROMAN_OS grows (more projects, team members, domains):

1. **New Team Members:** Read this document first, then domain CLAUDE.md
2. **New Skills:** Follow skill directory structure; add to relevant `.claude/skills/`
3. **New Agents:** Create with YAML header including `skills:` field
4. **New Domains:** Replicate COO/CMO structure; create domain CLAUDE.md
5. **Cross-Domain Work:** Use root-level files (`daily-roadmap.md`, `content-opportunities.md`)

**The 4L Principle applies at every decision:** Will this addition keep things Low Human, Low Cost, Low Complexity, Low Tech?

---

## Token Budget Guidelines

Context is finite. These guidelines help prioritize what to load.

### Component Token Targets

| Component | Target Tokens | Priority | Load When |
|-----------|---------------|----------|-----------|
| Root CLAUDE.md | ~2,500 | P0 - Always | Session start |
| Domain CLAUDE.md | ~2,000 | P1 - Domain entry | Entering COO/CMO |
| DOMAIN-STATUS.md | ~500 | P1 - Domain entry | Entering COO/CMO |
| WORKING.md | ~300 | P0 - Always | Session start |
| Skill SKILL.md | ~600 | P2 - On demand | Skill invocation |
| Skill knowledge/ | ~2,000 | P3 - If needed | Complex edge cases |
| Skill templates/ | Variable | P2 - On demand | Output generation |
| Project STATUS.md | ~400 | P2 - On demand | Project-specific work |
| Full project docs | ~5,000+ | P4 - Selective | Deep analysis only |
| Reference materials | ~3,000+ | P4 - Selective | Specific lookup |

### Priority Definitions

| Priority | Meaning | Pruning Behavior |
|----------|---------|------------------|
| P0 | Core context | Never prune |
| P1 | Domain context | Prune when switching domains |
| P2 | Task context | Prune when task complete |
| P3 | Supporting detail | Prune after use |
| P4 | Reference material | Load excerpts, not full docs |

### Loading Strategy

**Session Start:**
```
Load: CLAUDE.md + WORKING.md
Check: Which domain? → Load domain CLAUDE.md + DOMAIN-STATUS.md
Total: ~5,300 tokens (baseline)
```

**Task Execution:**
```
Identify skill/agent needed → Load SKILL.md (~600 tokens)
If edge case → Load knowledge/ excerpts (~500-1000 tokens)
Generate output → Load template
Total per task: ~1,500-2,500 additional tokens
```

**Deep Analysis:**
```
Load project full docs selectively
Use excerpts, not entire files
Summarize as you go
Budget: ~5,000 tokens for analysis context
```

### Warning Signs (Approaching Limits)

- Loading more than 3 full project files simultaneously
- Re-reading same file multiple times in session
- Response latency increasing
- Claude asking about already-discussed topics

### Pruning Checklist

When context feels heavy:

1. [ ] Have I summarized completed tasks to WORKING.md?
2. [ ] Am I holding full files that could be summarized?
3. [ ] Is there P3/P4 content loaded that's no longer needed?
4. [ ] Can I offload decision outcomes and clear deliberation?
5. [ ] Have I explicitly cleared context for unrelated tasks?

---

## Quick Reference

| I Need To... | Go To |
|--------------|-------|
| Understand the system | This document |
| See business context | `docs/business-context.md` |
| Troubleshoot issues | `docs/troubleshooting.md` |
| Work on operations | `COO/CLAUDE.md` |
| Work on content | `CMO/CLAUDE.md` |
| Check daily priorities | `daily-roadmap.md` |
| Log content opportunity | `content-opportunities.md` |
| Find a skill | `*/.claude/skills/` |
| Find an agent | `*/.claude/agents/` |

---

**Document Status:** Source of Truth
**Owner:** Donovan Proudfoot
**Philosophy:** 4L Principle (Low Human, Low Cost, Low Complexity, Low Tech)
