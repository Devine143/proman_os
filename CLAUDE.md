# PROMAN_OS

**Business OS for Proman Project Management, Cape Town**

---

## What This Is

Dual-domain AI operations system built on Claude Code:
- **COO Domain** - Construction project management operations
- **CMO Domain** - "The AI PM" newsletter and content marketing

**Flywheel:** Operations learnings → content → authority → clients → more operations

---

## Quick Reference

| Need | Location |
|------|----------|
| Operations | `COO/` |
| Content | `CMO/` |
| System Architecture | `docs/architecture/index.md` |
| Business Context | `docs/business-context.md` |
| Troubleshooting | `docs/troubleshooting.md` |

---

## Behavioral Defaults

Decision rules for ambiguous situations:

| Situation | Default Behavior |
|-----------|------------------|
| Uncertain which domain | Ask: "Is this COO (operations) or CMO (content)?" |
| Task scope unclear | Start small, confirm before expanding |
| Multiple valid approaches | Present 2-3 options with trade-offs, let CEO choose |
| Missing information | Ask for clarification |
| Multi-step work starting | Clarify domain → Create TodoWrite immediately |
| Financial/contractual decisions | Always escalate to CEO |
| Client-facing output | Draft first, never send without CEO review |

**Act vs. Ask Threshold:**
- **Act:** File organization, status updates, draft generation, research
- **Ask:** Anything involving money, clients, external parties, or irreversible actions

**When in doubt:** Bias toward asking. A 30-second clarification beats a 30-minute correction.

---

## Mode Commands

Behavioral mode switching for different task types:

| Command | Purpose | Tools Allowed |
|---------|---------|---------------|
| `/plan` | Strategic planning, no execution | Read, Glob, Grep, Task, Web |
| `/execute` | Implementation with verification | All modification tools |
| `/review` | Analysis and recommendations | Read-only tools |

**Workflow:** `/plan` → approve → `/execute` → `/review`

---

## Context Management

**Proactive compaction** - Don't wait for auto-compact at 95%.

| Context Level | Action |
|---------------|--------|
| 60-70% | Consider running `/compact` |
| 70-80% | Run `/compact`, preserve decisions and blockers |
| 80%+ | Immediate `/compact` required |

**What to preserve in compaction:**
- Decisions made and their rationale
- Current blockers and their status
- Progress state (what's done, what's next)
- Key file paths discovered

**What to discard:**
- Exploration details and search results
- Superseded plans
- Verbose tool outputs
- Completed task details

**Pre-compact checklist:**
1. Note any critical context in the compaction summary
2. Verify TodoWrite reflects actual progress

---

## Departments

### COO - Operations

Construction PM powered by Claude Code and PMP methodology.

**Details:** `COO/CLAUDE.md`

**Key Triggers:**
- "AI Project Status for [project]" → Client status report
- "AI LOI for [contractor]" → Letter of Intent
- "AI Budget Analysis for [project]" → Financial analysis

**Key Commands:**
| Command | Purpose |
|---------|---------|
| `/project-status` | Create client status report |

**Agents:** 5 specialized (doc-analyzer, project-docs-manager, etc.)

### CMO - Content

"The AI PM" newsletter - practical AI implementation for knowledge workers.

**Details:** `CMO/CLAUDE.md`

**Key Commands:**
| Command | Purpose |
|---------|---------|
| `/newsletter-post` | Create new post |
| `/free-post-outline` | Structure free tier content |
| `/newsletter-to-linkedin` | Repurpose to LinkedIn |
| `/performance-analysis` | Track engagement |

**Agents:** 6 specialized (LinkedIn Post Expander, Substack Notes Generator, etc.)

---

## Business Context

**Company:** Proman Project Management, Cape Town | **Model:** 2% of project value
**Goals:** R25M revenue, 2-3 staff, system-driven autonomy | **PMP Exam:** 21 Dec 2025

**Full details:** `docs/business-context.md`

---

## Cross-Domain Flywheel

COO implements workflow → Document learning → CMO creates content → Authority → Clients

---

## Support

1. Domain CLAUDE.md → 2. `docs/troubleshooting.md` → 3. `.claude/logs/` → 4. Escalate to CEO

---

**Version:** 5.2 - Fixed COO agent count after cleanup
**Last Updated:** 2025-11-30
