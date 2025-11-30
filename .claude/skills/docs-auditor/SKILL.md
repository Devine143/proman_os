---
name: docs-auditor
description: Audit CLAUDE.md and README.md files against actual system structure to identify discrepancies. Use when you hear "audit documentation", "check docs accuracy", "sync documentation", "verify CLAUDE.md", "verify README", or when docs feel out of date.
allowed-tools: Glob, Grep, Read, Write, Bash
---

# Documentation Auditor Skill

Compares CLAUDE.md and README.md documentation against actual repository structure to identify drift.

---

## What Gets Audited

| Component | Source of Truth | Documented In |
|-----------|-----------------|---------------|
| Agents | `.claude/agents/`, `*/agents/` | CLAUDE.md, README.md |
| Commands | `.claude/commands/`, `*/commands/` | CLAUDE.md, README.md |
| Skills | `.claude/skills/`, `*/skills/` | CLAUDE.md, README.md |
| Hooks | `.claude/hooks/*.py` | .claude/CLAUDE.md, README.md |
| SOPs | `*/sops/` | Domain CLAUDE.md, README.md |
| Directory structure | Actual folders | docs/architecture/, README.md |
| **Folder diagrams** | `ls` actual folders | Embedded ```tree``` blocks in CLAUDE.md |

---

## Workflow

### 1. Inventory Phase
```bash
# Count actual components
ls .claude/agents/*.md | wc -l
ls COO/.claude/agents/*.md | wc -l
ls CMO/.claude/agents/*.md | wc -l
# Repeat for commands, skills, hooks, SOPs
```

### 2. Documentation Phase
```bash
# Extract documented counts from CLAUDE.md and README.md files
grep -E "agents|commands|skills" */CLAUDE.md */README.md README.md
```

### 3. Folder Diagram Phase (CRITICAL)
```bash
# Find all tree diagrams in CLAUDE.md files (look for ├── or └──)
grep -B2 -A20 "├──\|└──" */CLAUDE.md .claude/CLAUDE.md CLAUDE.md 2>/dev/null

# For EACH diagram found:
# 1. Identify which folder it documents (e.g., "COO/", ".claude/", "projects/")
# 2. Run: ls -la <that-folder>/
# 3. Compare every line in diagram against actual folders
# 4. Flag any documented folder that doesn't exist
```

**Common failures:**
- "Project Structure" diagrams with fictional numbered folders
- `.claude/` diagrams listing non-existent `commands/`, `backups/`, `logs/`
- Domain diagrams with removed SOPs or templates folders

### 4. Compare Phase
Generate discrepancy report using [audit-report template](templates/audit-report.md).

### 5. Fix Phase (Optional)
Update CLAUDE.md and README.md files with accurate counts and component lists.

---

## Audit Commands

| Command | Purpose |
|---------|---------|
| Full audit | Check all components across all domains |
| Domain audit | Check single domain (COO, CMO, or root) |
| Component audit | Check single type (agents, commands, etc.) |

---

## Output

See [templates/audit-report.md](templates/audit-report.md) for report format.

**Quick summary format:**
```
## Audit Results: [timestamp]

| Area | Documented | Actual | Status |
|------|------------|--------|--------|
| Agents (root) | 5 | 6 | DRIFT |
| Agents (COO) | 10 | 11 | DRIFT |
| Commands (CMO) | 7 | 29 | DRIFT |

### Fixes Required:
1. [file]: Update X from Y to Z
```

---

## Integration

**When to run:**
- After adding/removing agents, commands, skills
- Before major releases
- Monthly maintenance
- When documentation "feels wrong"

**Auto-trigger phrases:**
- "audit documentation"
- "check docs accuracy"
- "is documentation up to date"
- "sync docs with reality"
- "verify README"

---

## Examples

### Example 1: Full System Audit

User request:
```
Audit the documentation
```

You would:
1. Read [audit-checklist.md](reference/audit-checklist.md) for component locations
2. Count actual components:
   ```bash
   ls -1 .claude/agents/*.md | wc -l
   ls -1 .claude/commands/*.md | wc -l
   ls -d .claude/skills/*/ | wc -l
   ls -1 .claude/hooks/*.py | wc -l
   ```
3. Read each CLAUDE.md file and extract documented counts
4. **Validate folder diagrams:** Find all tree structures (├── └──) and verify each folder exists
5. Compare actual vs documented, noting discrepancies
6. Generate report using [audit-report.md](templates/audit-report.md) format
7. Present findings with copy-paste fixes

### Example 2: Single Domain Audit

User request:
```
Check if COO documentation is accurate
```

You would:
1. Focus only on COO domain:
   ```bash
   ls -1 COO/.claude/agents/*.md | wc -l
   ls -1 COO/.claude/commands/*.md | wc -l
   ls -1 COO/sops/*.md | wc -l
   ```
2. Read `COO/CLAUDE.md` and extract documented counts
3. Compare and report discrepancies for COO only

### Example 3: Component-Specific Audit

User request:
```
Are all hooks documented correctly?
```

You would:
1. List actual hook files:
   ```bash
   ls -1 .claude/hooks/*.py
   ```
2. Read `.claude/CLAUDE.md` hooks table
3. Map documented names to actual files
4. Report any missing or extra entries

---

## References

- [Audit Checklist](reference/audit-checklist.md) - What to check
- [Report Template](templates/audit-report.md) - Output format
- [Sample Audit](examples/sample-audit.md) - Example output

---

**Version:** 1.2 - Added folder diagram validation phase
**Last Updated:** 2025-11-30
