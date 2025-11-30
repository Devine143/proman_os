# PROMAN_OS Architecture

**Source of truth for system design. Load details on demand.**

---

## Quick Navigation

| Topic | File | When to Load |
|-------|------|--------------|
| Core philosophy (4L) | [principles.md](principles.md) | Understanding design decisions |
| Skills & Agents | [components.md](components.md) | Creating/modifying agents or skills |
| Hooks & Automation | [hooks.md](hooks.md) | Configuring automation |
| Folder structure | [structure.md](structure.md) | File organization questions |
| Data flows | [flows.md](flows.md) | Understanding system integration |
| Token budgets | [token-budget.md](token-budget.md) | Context optimization |
| Standards | [standards.md](standards.md) | Naming, status indicators, backups |

---

## Core Philosophy: 4L Principle

Every architectural decision follows four constraints:

| Principle | Meaning |
|-----------|---------|
| **Low Human** | AI handles operations; minimize manual intervention |
| **Low Cost** | Claude Code as engine; avoid tool sprawl |
| **Low Complexity** | Components compose cleanly; avoid over-engineering |
| **Low Tech** | SOPs become executable skills; operators don't code |

**Details:** [principles.md](principles.md)

---

## Key Patterns

### Progressive Disclosure
Load minimum to route, discover details as needed.
```
CLAUDE.md (lean hub) → "For X, see docs/..." → Load on demand
```

### Skills = Executable SOPs
```
skill-name/
├── SKILL.md      # Entry point
├── knowledge/    # Reference docs
├── templates/    # Output formats
└── scripts/      # Automation
```

### Agent + Skill Combo
Agent provides judgment; skill provides playbook.

**Details:** [components.md](components.md)

---

## System Layout

```
PROMAN_OS/
├── CLAUDE.md              # Root hub
├── docs/architecture/     # THIS DIRECTORY
├── COO/                   # Operations domain
├── CMO/                   # Content domain
└── .claude/               # Configuration
    ├── agents/            # Cross-domain agents
    ├── skills/            # Shared skills
    ├── commands/          # CEO commands
    └── hooks/             # Automation
```

**Full structure:** [structure.md](structure.md)

---

## Token Targets

| Component | Tokens | Priority |
|-----------|--------|----------|
| Root CLAUDE.md | ~2,500 | P0 - Always load |
| Domain CLAUDE.md | ~2,000 | P1 - Domain entry |
| Skill SKILL.md | ~600 | P2 - On demand |

**Full guidelines:** [token-budget.md](token-budget.md)

---

**Version:** 4.0 - Progressive Disclosure Refactor
**Last Updated:** 2025-11-29
