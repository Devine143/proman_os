---
type: reference
purpose: Detailed checklist of what to audit and how
last_updated: 2025-11-30
version: 1.1 - Added folder diagram validation section
---

# Audit Checklist

## 1. Agent Inventory

### Locations to Check
```
.claude/agents/           # Cross-domain agents
COO/.claude/agents/       # COO-specific agents
CMO/.claude/agents/       # CMO-specific agents
```

### Documentation Sources
| File | Section to Check |
|------|------------------|
| `/CLAUDE.md` | "Departments" section, agent counts |
| `/README.md` | Project overview, component mentions |
| `/.claude/CLAUDE.md` | "Agents" table |
| `/COO/CLAUDE.md` | "Agents" or key agents list |
| `/CMO/CLAUDE.md` | "Agents" or key agents list |

### Verification Commands
```bash
# Count cross-domain agents
ls -1 .claude/agents/*.md 2>/dev/null | wc -l
ls -1 .claude/agents/*/*.md 2>/dev/null | grep -v "procedures\|examples\|output" | wc -l

# Count COO agents
ls -1 COO/.claude/agents/*.md 2>/dev/null | wc -l

# Count CMO agents
ls -1 CMO/.claude/agents/*.md 2>/dev/null | wc -l

# List all agent names
find . -path "*/.claude/agents/*.md" -type f | xargs -I{} basename {} .md | sort
```

---

## 2. Command Inventory

### Locations to Check
```
.claude/commands/         # Cross-domain commands
COO/.claude/commands/     # COO-specific commands
CMO/.claude/commands/     # CMO-specific commands
```

### Documentation Sources
| File | Section to Check |
|------|------------------|
| `/CLAUDE.md` | "Mode Commands" table |
| `/README.md` | Usage section, command examples |
| `/.claude/CLAUDE.md` | "Commands" table |
| `/COO/CLAUDE.md` | "Key Commands" section |
| `/CMO/CLAUDE.md` | "Key Commands" section |

### Verification Commands
```bash
# Count commands per location
ls -1 .claude/commands/*.md 2>/dev/null | wc -l
ls -1 COO/.claude/commands/*.md 2>/dev/null | wc -l
ls -1 CMO/.claude/commands/*.md 2>/dev/null | wc -l

# List all command names (without extension)
find . -path "*/.claude/commands/*.md" -type f | xargs -I{} basename {} .md | sort
```

---

## 3. Skill Inventory

### Locations to Check
```
.claude/skills/           # Cross-domain skills
COO/.claude/skills/       # COO-specific skills
CMO/.claude/skills/       # CMO-specific skills
```

### Documentation Sources
Skills are often underdocumented. Check:
- Any "Skills" sections in CLAUDE.md files
- Any "Skills" sections in README.md files
- `docs/architecture/components.md` if exists

### Verification Commands
```bash
# Count skill folders (skills are typically folders)
ls -d .claude/skills/*/ 2>/dev/null | wc -l
ls -d COO/.claude/skills/*/ 2>/dev/null | wc -l
ls -d CMO/.claude/skills/*/ 2>/dev/null | wc -l

# List all skill names
find . -path "*/.claude/skills/*/SKILL.md" -type f | xargs -I{} dirname {} | xargs -I{} basename {}
```

---

## 4. Hook Inventory

### Location
```
.claude/hooks/            # All hooks (Python files)
```

### Documentation Source
- `/.claude/CLAUDE.md` - "Hooks" table
- `/README.md` - Setup/installation sections

### Verification Commands
```bash
# Count Python hook files
ls -1 .claude/hooks/*.py 2>/dev/null | wc -l

# List hook names
ls -1 .claude/hooks/*.py 2>/dev/null | xargs -I{} basename {} .py | sort
```

### Common Discrepancy
Documentation often uses conceptual names (e.g., "pre-tool-backup") while actual files use Python naming (e.g., "pre_tool_use.py"). Map both.

---

## 5. SOP Inventory

### Locations to Check
```
COO/sops/                 # COO Standard Operating Procedures
CMO/sops/                 # CMO SOPs (if any)
```

### Documentation Source
- `/COO/CLAUDE.md` - "SOPs" section
- `/CMO/CLAUDE.md` - "SOPs" section (if applicable)

### Verification Commands
```bash
# Count SOPs
ls -1 COO/sops/*.md 2>/dev/null | wc -l
ls -1 CMO/sops/*.md 2>/dev/null | wc -l

# List SOP names
ls -1 COO/sops/sop-*.md 2>/dev/null | xargs -I{} basename {} .md | sed 's/sop-//'
```

---

## 6. Folder Structure Diagrams (CRITICAL)

### What to Check
Any tree diagram in CLAUDE.md files using `├──` or `└──` characters.

### How to Find Them
```bash
# Find all tree diagrams
grep -n "├──\|└──" */CLAUDE.md .claude/CLAUDE.md CLAUDE.md 2>/dev/null
```

### Validation Process
For each diagram found:
1. Identify the root folder (look at line before the tree starts)
2. Extract all folder names from the diagram
3. Run `ls -la <root-folder>/` to see actual contents
4. Compare line by line

### Common Failures
| Documented | Reality | Fix |
|------------|---------|-----|
| `00-inbox/`, `01-initiation/` | Folder deleted or renamed | Remove from diagram |
| `sops/`, `templates/` | Never existed or deleted | Remove from diagram |
| `commands/`, `backups/` | Folder doesn't exist | Remove from diagram |

### Example
```
# COO/CLAUDE.md documents:
projects/[project-name]/
├── 00-inbox/
├── 01-initiation/

# But actual project has:
$ ls COO/projects/11_Buck_Road/
00_Inbox  docs  initiation  project-management

# DRIFT: Diagram is fictional
```

---

## 7. Architecture Documentation

### Files to Verify
```
docs/architecture/
├── index.md              # Should match actual structure
├── structure.md          # Directory layout claims
├── components.md         # Agent/skill/command lists
├── hooks.md              # Hook documentation
└── flows.md              # Data flow diagrams
```

### Common Issues
- References to removed files (WORKING.md, DOMAIN-STATUS.md)
- Outdated directory trees
- Wrong component counts

---

## 8. Cross-Reference Checks

### Internal Links
Verify all `[text](path)` links in CLAUDE.md and README.md files point to existing files.

```bash
# Extract markdown links and check existence
grep -oE '\[.*\]\([^)]+\)' CLAUDE.md README.md | grep -oE '\([^)]+\)' | tr -d '()'
```

### Trigger Phrases
Ensure triggers documented in YAML headers match actual routing.

---

## 9. Version Consistency

Check all CLAUDE.md and README.md files have:
- Matching "Last Updated" dates if batch-updated
- Consistent version numbering scheme
- Accurate "Removed X" notes

---

## Audit Frequency Recommendations

| Trigger | Scope |
|---------|-------|
| After adding/removing component | Affected domain only |
| Weekly maintenance | Quick count check |
| Monthly review | Full audit |
| Before documentation release | Full audit + link check |
