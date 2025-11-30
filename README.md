# PROMAN_OS

**Business Operating System for Proman Project Management**

A dual-domain AI-powered operations system built on Claude Code, designed to manage construction project operations and content marketing for Proman Project Management, Cape Town.

---

## Overview

PROMAN_OS is a comprehensive business operating system that combines:

- **COO Domain** - Construction project management operations powered by PMP methodology
- **CMO Domain** - "The AI PM" newsletter and content marketing operations

The system operates on a flywheel model: **Operations learnings → Content → Authority → Clients → More operations**

---

## Repository Structure

```
PROMAN_OS/
├── COO/              # Construction Operations domain
│   ├── projects/     # Active project files
│   ├── references/   # JBCC contracts, case law, negotiation guides
│   ├── scripts/      # Python utilities for document processing
│   └── CLAUDE.md     # Domain-specific AI instructions
│
├── CMO/              # Content Marketing domain
│   ├── newsletter-drafts/    # Draft content
│   ├── linkedin-posts/       # Social media content
│   ├── new-post-ideas/       # Content pipeline
│   └── CLAUDE.md             # Domain-specific AI instructions
│
├── docs/             # System documentation
│   ├── architecture/  # System architecture and design
│   ├── learnings/    # Workflows, decisions, and gotchas
│   └── examples/     # Usage examples
│
└── .claude/          # Claude Code configuration
    ├── agents/        # Specialized AI agents
    ├── commands/     # Custom commands
    └── hooks/        # System hooks and utilities
```

---

## Branch Structure

This repository uses a multi-branch approach:

- **`main`** - Root structure with shared documentation and system configuration
- **`coo`** - Main branch + COO domain (construction operations)
- **`cmo`** - Main branch + CMO domain (content marketing)

This structure allows independent development of each domain while maintaining shared infrastructure.

---

## Quick Start

### For Developers

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Devine143/proman_os.git
   cd proman_os
   ```

2. **Checkout the branch you need:**
   ```bash
   git checkout main    # Root structure only
   git checkout coo     # Construction operations
   git checkout cmo     # Content marketing
   ```

3. **Review domain-specific documentation:**
   - Root: `CLAUDE.md`
   - COO: `COO/CLAUDE.md`
   - CMO: `CMO/CLAUDE.md`

### For AI Assistants

The system uses Claude Code with domain-specific instructions. Key entry points:

- **Root instructions:** `CLAUDE.md`
- **COO domain:** `COO/CLAUDE.md`
- **CMO domain:** `CMO/CLAUDE.md`
- **System architecture:** `docs/architecture/index.md`
- **Workflows:** `docs/learnings/workflows/`

**Critical:** Always check `docs/learnings/` before executing any workflow to see if an established process exists.

---

## Key Features

### COO Domain (Construction Operations)

- **Project Management:** Status reports, budget analysis, contract review
- **Document Processing:** PDF extraction, Excel automation, document analysis
- **Reference Library:** JBCC contracts, case law, negotiation frameworks
- **Specialized Agents:** Document analyzer, project docs manager, and more

**Key Commands:**
- `/project-status` - Generate client status reports
- Document analysis and processing utilities

### CMO Domain (Content Marketing)

- **Newsletter Creation:** "The AI PM" newsletter content generation
- **Content Repurposing:** Newsletter to LinkedIn, Twitter threads
- **Performance Tracking:** Engagement analytics and optimization
- **Specialized Agents:** LinkedIn Post Expander, Substack Notes Generator, and more

**Key Commands:**
- `/newsletter-post` - Create new newsletter content
- `/newsletter-to-linkedin` - Repurpose content for LinkedIn
- `/performance-analysis` - Track engagement metrics

---

## Documentation

| Resource | Location | Purpose |
|----------|----------|---------|
| System Architecture | `docs/architecture/` | Technical design and structure |
| Business Context | `docs/business-context.md` | Company overview and goals |
| Workflows | `docs/learnings/workflows/` | Established processes |
| Decisions | `docs/learnings/decisions/` | Rationale for choices |
| Gotchas | `docs/learnings/gotchas/` | Common errors and solutions |
| Troubleshooting | `docs/troubleshooting.md` | Problem resolution |

---

## Business Context

**Company:** Proman Project Management, Cape Town, South Africa  
**Model:** 2% of project value  
**Goals:** R25M revenue, 2-3 staff, system-driven autonomy  
**PMP Certification:** Exam scheduled 21 December 2025

For detailed business information, see `docs/business-context.md`.

---

## Technology Stack

- **AI Framework:** Claude Code (Anthropic)
- **Python Management:** `uv` and `uvx` (no direct Python installation)
- **Platform:** macOS (Apple Silicon M4 Max)
- **Automation:** AppleScript for OS-level automation

---

## Contributing

This is a private repository for Proman Project Management operations. For questions or access requests, contact the repository owner.

---

## License

Private repository - All rights reserved.

---

## Support

1. Check domain-specific `CLAUDE.md` files
2. Review `docs/troubleshooting.md`
3. Check `.claude/logs/` for system logs
4. Escalate to repository owner

---

**Version:** 1.0  
**Last Updated:** 2025-11-30

