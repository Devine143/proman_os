---
type: example
purpose: Real audit output from 2025-11-30 system review
last_updated: 2025-11-30
---

# Sample Audit Report

This is a real audit performed on 2025-11-30.

---

# Documentation Audit Report

**Date:** 2025-11-30
**Scope:** Full
**Auditor:** Claude Code

---

## Executive Summary

12 discrepancies found across agents, commands, skills, hooks, and SOPs. Documentation has drifted from actual system state.

**Status:** DRIFT DETECTED

---

## Component Inventory

### Agents

| Location | Documented | Actual | Delta | Status |
|----------|------------|--------|-------|--------|
| .claude/agents/ | 5 | 6 | +1 | DRIFT |
| COO/.claude/agents/ | 10 (root) / 5 (COO) | 11 | +1/+6 | DRIFT |
| CMO/.claude/agents/ | 6 (root) / 4 (CMO) | 6 | 0/+2 | DRIFT |
| **Total** | **21** | **23** | **+2** | |

**Missing from docs:**
- `.claude/agents/project-curator.md` - not listed in .claude/CLAUDE.md
- COO agents undercounted in COO/CLAUDE.md (lists 5, has 11)

### Commands

| Location | Documented | Actual | Delta | Status |
|----------|------------|--------|-------|--------|
| .claude/commands/ | 3 | 4 | +1 | DRIFT |
| COO/.claude/commands/ | 0 | 5 | +5 | DRIFT |
| CMO/.claude/commands/ | 7 | 29 | +22 | DRIFT |
| **Total** | **10** | **38** | **+28** | |

**Missing from docs:**
- `.claude/commands/note-reply.md` - not documented
- All 5 COO commands undocumented in root CLAUDE.md
- 22 CMO commands not listed (only 7 highlighted)

### Skills

| Location | Documented | Actual | Delta | Status |
|----------|------------|--------|-------|--------|
| .claude/skills/ | 1 | 2 | +1 | DRIFT |
| COO/.claude/skills/ | ~2 | 8 | +6 | DRIFT |
| CMO/.claude/skills/ | 0 | 5 | +5 | DRIFT |
| **Total** | **~3** | **15** | **+12** | |

Skills barely documented in any CLAUDE.md file.

### Hooks

| Documented Name | Actual File | Status |
|-----------------|-------------|--------|
| pre-tool-backup | pre_tool_use.py | MISMATCH |
| post-tool-log | post_tool_use.py | MISMATCH |
| subagent-quality-gate | subagent_stop.py | MISMATCH |
| session-end-cleanup | session_end.py | MISMATCH |
| pre-compact-save-state | pre_compact.py | MISMATCH |
| (not documented) | notification.py | MISSING |
| (not documented) | send_event.py | MISSING |
| (not documented) | stop.py | MISSING |
| (not documented) | test_hitl.py | MISSING |
| (not documented) | user_prompt_submit.py | MISSING |

### SOPs

| Domain | Documented | Actual | Delta | Status |
|--------|------------|--------|-------|--------|
| COO | 6 | 8 | +2 | DRIFT |
| CMO | 0 | 0 | 0 | OK |

**Missing from docs:**
- `sop-consultant-selection-onboarding.md`
- `sop-negotiation-debrief.md`

---

## Discrepancies Detail

### 1. Agent Count in .claude/CLAUDE.md

**File:** `/.claude/CLAUDE.md`
**Current:** Lists 5 agents
**Should be:** 6 agents (add project-curator)
**Fix:** Add `| project-curator | Project curation |` to agents table

### 2. Agent Count in Root CLAUDE.md

**File:** `/CLAUDE.md`
**Current:** "10 specialized (procurement-manager, client-relations, financial-controller, etc.)"
**Should be:** "11 specialized agents"
**Fix:** Update count from 10 to 11

### 3. COO Agent List in COO/CLAUDE.md

**File:** `/COO/CLAUDE.md`
**Current:** Lists 5 key agents
**Should be:** Should mention 11 total exist
**Fix:** Add note: "11 specialized agents (5 key agents highlighted below)"

### 4. Hook Names in .claude/CLAUDE.md

**File:** `/.claude/CLAUDE.md`
**Current:** Uses conceptual names (pre-tool-backup, etc.)
**Should be:** Match actual Python filenames
**Fix:** Update hooks table with actual filenames

### 5. Missing SOPs in COO/CLAUDE.md

**File:** `/COO/CLAUDE.md`
**Current:** Lists 6 SOPs
**Should be:** 8 SOPs
**Fix:** Add sop-consultant-selection-onboarding, sop-negotiation-debrief

### 6. Architecture Docs Reference Removed Files

**File:** `docs/architecture/structure.md`, `docs/architecture/token-budget.md`
**Current:** Reference WORKING.md, DOMAIN-STATUS.md
**Should be:** Remove references (files were deleted per version notes)
**Fix:** Remove all mentions of WORKING.md and DOMAIN-STATUS.md

---

## Recommendations

### Immediate Fixes

1. **/.claude/CLAUDE.md:** Add project-curator to agents table
2. **/.claude/CLAUDE.md:** Update hook names to match actual Python files
3. **/CLAUDE.md:** Change COO agent count "10" → "11"
4. **/COO/CLAUDE.md:** Change SOP count "6" → "8", add missing 2
5. **/COO/CLAUDE.md:** Clarify "5 key agents" vs "11 total agents"
6. **docs/architecture/*.md:** Remove WORKING.md/DOMAIN-STATUS.md references

### Structural Improvements

- Consider adding a "Skills" section to CLAUDE.md files (currently 15 skills undocumented)
- Consider documenting COO and CMO commands more comprehensively
- Standardize hook naming: either use Python filenames everywhere OR create aliases

---

**Audit Complete**
