---
type: template
purpose: Standard output format for documentation audits
last_updated: 2025-11-30
---

# Audit Report Template

Use this format when reporting audit results.

---

## Template

```markdown
# Documentation Audit Report

**Date:** YYYY-MM-DD
**Scope:** [Full | Domain: X | Component: Y]
**Auditor:** Claude Code

---

## Executive Summary

[1-2 sentence overview: X discrepancies found across Y components]

**Status:** [CURRENT | DRIFT DETECTED | CRITICAL DRIFT]

---

## Component Inventory

### Agents

| Location | Documented | Actual | Delta | Status |
|----------|------------|--------|-------|--------|
| .claude/agents/ | X | Y | +/-Z | [OK|DRIFT] |
| COO/.claude/agents/ | X | Y | +/-Z | [OK|DRIFT] |
| CMO/.claude/agents/ | X | Y | +/-Z | [OK|DRIFT] |
| **Total** | **X** | **Y** | **+/-Z** | |

**Missing from docs:** [list actual agents not documented]
**Documented but missing:** [list documented agents that don't exist]

### Commands

| Location | Documented | Actual | Delta | Status |
|----------|------------|--------|-------|--------|
| .claude/commands/ | X | Y | +/-Z | [OK|DRIFT] |
| COO/.claude/commands/ | X | Y | +/-Z | [OK|DRIFT] |
| CMO/.claude/commands/ | X | Y | +/-Z | [OK|DRIFT] |
| **Total** | **X** | **Y** | **+/-Z** | |

### Skills

| Location | Documented | Actual | Delta | Status |
|----------|------------|--------|-------|--------|
| .claude/skills/ | X | Y | +/-Z | [OK|DRIFT] |
| COO/.claude/skills/ | X | Y | +/-Z | [OK|DRIFT] |
| CMO/.claude/skills/ | X | Y | +/-Z | [OK|DRIFT] |
| **Total** | **X** | **Y** | **+/-Z** | |

### Hooks

| Documented Name | Actual File | Status |
|-----------------|-------------|--------|
| [conceptual-name] | [actual_file.py] | [MATCH|MISMATCH|MISSING] |

### SOPs

| Domain | Documented | Actual | Delta | Status |
|--------|------------|--------|-------|--------|
| COO | X | Y | +/-Z | [OK|DRIFT] |
| CMO | X | Y | +/-Z | [OK|DRIFT] |

---

## Discrepancies Detail

### [Category]: [Specific Issue]

**File:** `path/to/file.md`
**Line:** [if applicable]
**Current:** [what it says]
**Should be:** [what it should say]
**Fix:** [specific edit needed]

[Repeat for each discrepancy]

---

## Broken Links

| File | Link | Target | Status |
|------|------|--------|--------|
| path/file.md | [text](target) | target | [OK|BROKEN] |

---

## Recommendations

### Immediate Fixes (Copy-Paste Ready)

1. **[File]:** Change "[old text]" to "[new text]"
2. **[File]:** Add "[missing component]" to [section]
3. **[File]:** Remove reference to "[deleted item]"

### Structural Improvements

- [Any architectural suggestions]

---

## Files Modified (If Auto-Fixed)

| File | Changes Made |
|------|--------------|
| path/to/file.md | Updated agent count from X to Y |

---

**Audit Complete**
```

---

## Status Definitions

| Status | Meaning | Action |
|--------|---------|--------|
| CURRENT | Docs match reality | None |
| DRIFT | Minor discrepancies | Update within 1 week |
| CRITICAL DRIFT | Major gaps or broken links | Update immediately |

---

## Quick Summary Format

For brief reports, use this condensed format:

```markdown
## Audit: [date]

| Area | Doc | Actual | Status |
|------|-----|--------|--------|
| Agents (root) | 5 | 6 | DRIFT |
| Agents (COO) | 10 | 11 | DRIFT |
| Commands (CMO) | 7 | 29 | DRIFT |

**Fixes needed:**
1. `/.claude/CLAUDE.md`: agents 5→6
2. `/CLAUDE.md`: COO agents 10→11
3. `/CMO/CLAUDE.md`: add 22 missing commands
```
