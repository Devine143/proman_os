# System Components

**Skills, agents, and their interaction patterns**

---

## Skills: Executable SOPs

**Problem:** SOPs as flat markdown are passive - Claude reads them but can't execute deterministically.

**Solution:** Skills package knowledge + templates + scripts into executable units.

### Skill Directory Structure

```
skill-name/
├── SKILL.md        # YAML header + process overview
├── knowledge/      # Reference docs, examples, edge cases
├── templates/      # Output templates (docx, md, xlsx)
└── scripts/        # Deterministic code
```

### YAML Header (enables auto-invocation)

```yaml
---
name: docs-auditor
description: Audit CLAUDE.md and README.md files against actual system
  structure. Use when you hear "audit documentation", "check docs accuracy".
allowed-tools: Glob, Grep, Read, Write, Bash
---
```

### How Auto-Invocation Works

1. User says "Audit the documentation"
2. Claude recognizes "audit" matches skill description
3. Skill loads → provides process, templates, scripts
4. Output is consistent and deterministic

---

## Agents

**Characteristics:**
- Specialized expertise (one job, done well)
- Context isolation (don't pollute main conversation)
- Equipped with relevant skills
- YAML headers define capabilities

### Agent Distribution

| Location | Count | Examples |
|----------|-------|----------|
| Root `.claude/agents/` | 6 | ceo-briefing, workflow-optimizer |
| COO `.claude/agents/` | 11 | procurement-manager, financial-controller |
| CMO `.claude/agents/` | 6 | linkedin-post-expander, newsletter-analyst |

### Required YAML Header

```yaml
---
name: procurement-manager
description: Handles contractor procurement, quotes, negotiations
tools:
  - Read
  - Write
  - Bash
  - Task
skills:
  - docx
  - pdf
model: sonnet
---
```

---

## The Power Combo: Agents + Skills

**Problem:** Agents are smart but lack formalized processes. Skills have processes but lack judgment.

**Solution:** Equip agents with skills. Agent provides judgment; skill provides playbook.

### Execution Flow

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

## Commands

**Trigger Pattern:** `/command-name`

| Type | Location | Examples |
|------|----------|----------|
| CEO | Root `.claude/commands/` | `/daily-briefing`, `/weekly-review` |
| COO | `COO/.claude/commands/` | `/project-status`, `/analyze_large_doc` |
| CMO | `CMO/.claude/commands/` | `/newsletter-post`, `/newsletter-to-linkedin` |

---

## Skills (Actual)

| Skill | Domain | Purpose |
|-------|--------|---------|
| docx | Shared | Word document creation/editing |
| pdf | Shared | PDF processing and forms |
| pptx | Shared | PowerPoint presentations |
| xlsx | Shared | Excel spreadsheets |
| docs-auditor | Root | Audit documentation accuracy |
| meta-skill | Root/CMO | Create new skills |

---

**Version:** 1.0
**Last Updated:** 2025-11-29
