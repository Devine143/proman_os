# Token Budget Guidelines

**Context is finite. These guidelines help prioritize what to load.**

---

## Component Token Targets

| Component | Target Tokens | Priority | Load When |
|-----------|---------------|----------|-----------|
| Root CLAUDE.md | ~2,500 | P0 - Always | Session start |
| Domain CLAUDE.md | ~2,000 | P1 - Domain entry | Entering COO/CMO |
| Skill SKILL.md | ~600 | P2 - On demand | Skill invocation |
| Skill knowledge/ | ~2,000 | P3 - If needed | Complex edge cases |
| Skill templates/ | Variable | P2 - On demand | Output generation |
| Project STATUS.md | ~400 | P2 - On demand | Project-specific work |
| Full project docs | ~5,000+ | P4 - Selective | Deep analysis only |
| Reference materials | ~3,000+ | P4 - Selective | Specific lookup |

---

## Priority Definitions

| Priority | Meaning | Pruning Behavior |
|----------|---------|------------------|
| P0 | Core context | Never prune |
| P1 | Domain context | Prune when switching domains |
| P2 | Task context | Prune when task complete |
| P3 | Supporting detail | Prune after use |
| P4 | Reference material | Load excerpts, not full docs |

---

## File Size Limits

| File Type | Max Lines | Action if Exceeded |
|-----------|-----------|-------------------|
| CLAUDE.md | 200 lines | Split to docs/ references |
| Agent (core) | 80 lines | Create agent subfolder |
| Skill entry | 150 lines | Use reference/ subfolders |
| SOP | 200 lines | Split into phases |
| Any .md | 300 lines | Mandatory refactor |

---

## Warning Signs (Approaching Limits)

- Loading more than 3 full project files simultaneously
- Re-reading same file multiple times in session
- Response latency increasing
- Claude asking about already-discussed topics

---

## Pruning Checklist

When context feels heavy:

- [ ] Summarized completed tasks?
- [ ] Holding full files that could be summarized?
- [ ] P3/P4 content loaded that's no longer needed?
- [ ] Can offload decision outcomes and clear deliberation?
- [ ] Explicitly cleared context for unrelated tasks?

---

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| Inline examples in agent files | Bloats context | Move to examples/ subfolder |
| Full SOPs in CLAUDE.md | Loads every session | Reference sops/ folder |
| Detailed formats in core file | Unnecessary upfront | Move to output-formats.md |
| No YAML headers | Can't search/filter | Add standard header |
| Monolithic 500+ line files | Context pollution | Split by concern |

---

**Version:** 1.1 - Removed WORKING.md/DOMAIN-STATUS.md references
**Last Updated:** 2025-11-30
