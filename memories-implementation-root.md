# Phase 1: Root Memory System Implementation

**Location:** `/Users/donovan/PROMAN_OS/memories/`

---

## Memory → Agent/Skill Promotion Pipeline

The purpose of memories is to **capture and validate workflows before investing in automation**.

```
Ad-hoc task
    ↓
Document in memories/ (low effort)
    ↓
Track usage frequency + success rate
    ↓
If used 5+ times with high success → Candidate for promotion
    ↓
Promote to Agent (if needs autonomy) or Skill (if needs structure)
```

### Promotion Criteria

| Metric | Threshold | Action |
|--------|-----------|--------|
| Usage | 5+ times | Review for promotion |
| Success rate | 80%+ | Good candidate |
| Time per use | >15 min | Worth automating |
| Complexity | Multi-step | Better as agent/skill |

### Memory File Tracking Fields

Every memory file includes:
- **Last used:** [Date] - track recency
- **Use count:** [N] - track frequency (increment manually)
- **Success rate:** [High/Medium/Low] - track reliability
- **Promotion status:** [Memory / Candidate / Promoted to @agent or skill:name]

### When to Promote

**To Agent:** Workflow needs autonomy, context gathering, decision-making
- Example: `loi-creation.md` → `@loi-generator` agent

**To Skill:** Workflow needs structure, templates, consistent output
- Example: `status-reports.md` → `skill:client-status-report`

---

## Directory Structure to Create

```
PROMAN_OS/memories/
├── README.md
├── domain-handoffs/
│   ├── content-opportunities.md    # THE FLYWHEEL BUFFER
│   └── cmo-to-coo.md
├── flywheel/
│   └── complete-cycles.md
├── context-management/
│   └── compaction-strategies.md
└── ceo-decisions/
    └── act-vs-ask.md
```

---

## Files to Create

### 1. `memories/README.md`

```markdown
# PROMAN_OS Cross-Domain Workflow Memory

Search here FIRST before multi-step tasks.

## Quick Index

| Category | Location | When to Use |
|----------|----------|-------------|
| COO → CMO handoffs | `domain-handoffs/content-opportunities.md` | Log content-worthy COO insights |
| CMO → COO insights | `domain-handoffs/cmo-to-coo.md` | Content reveals ops improvement |
| Flywheel tracking | `flywheel/complete-cycles.md` | Track COO → CMO → Authority → Client |
| Context management | `context-management/` | 70%+ context, compaction needed |
| CEO decisions | `ceo-decisions/act-vs-ask.md` | Uncertain if should act or ask |

## Domain-Specific Memories

| Domain | Location | Purpose |
|--------|----------|---------|
| Operations | `../COO/memories/` | Procurement, budgets, clients |
| Content | `../CMO/memories/` | Newsletter, repurposing, performance |

## How to Search

```bash
# Cross-domain patterns
grep -ri "[keyword]" memories/

# Operations workflows
grep -ri "[keyword]" COO/memories/

# Content workflows
grep -ri "[keyword]" CMO/memories/

# Check flywheel buffer
cat memories/domain-handoffs/content-opportunities.md
```

## Execution Loop

1. **SEARCH** - Check memories before starting task
2. **DECIDE** - Use existing workflow OR plan new approach
3. **EXECUTE** - Follow workflow steps
4. **CAPTURE** - Update memory with learnings
```

---

### 2. `memories/domain-handoffs/content-opportunities.md`

```markdown
# Content Opportunities from Operations

**Purpose:** The flywheel buffer - log content-worthy operational learnings for CMO pipeline.

**Status Key:**
- 🟢 Ready for CMO - Logged, not yet drafted
- 🟡 In progress - CMO drafting
- ✅ Published - Live content
- ❌ Archived - Not pursued

---

## How to Use

**COO (after completing workflow):**
1. Ask: "Could this become newsletter content?"
2. If YES → Add entry below with 🟢 status
3. Link to your COO memory file

**CMO (during content planning):**
1. Check this file for 🟢 Ready entries
2. Select one, change to 🟡 In progress
3. After publishing, change to ✅ Published

---

## Template for New Entry

```
## [Workflow Name] (Logged: YYYY-MM-DD)

**Status:** 🟢 Ready for CMO
**Source:** [Project/task description]
**COO memory:** `COO/memories/[category]/[file].md`

### What Happened
[2-3 sentence summary of situation and solution]

### Content Angles

**Free Tier (What + Why):**
- Title idea: "[Hook-based title with specific number/outcome]"
- Angle: [The insight or principle]
- Target: [Who this helps]

**Paid Tier (How to Build):**
- Title idea: "[Implementation-focused title]"
- Angle: [Step-by-step guide]
- Target: [Who wants to build this]

### Supporting Details
- PMP connection: [Process/principle]
- AI element: [Claude Code/automation]
- Real impact: [R amount, % saved, days reduced]

### CMO Notes
[Space for CMO to add content planning notes after selection]
```

---

## Logged Opportunities

<!-- Add new entries above this line -->
```

---

### 3. `memories/domain-handoffs/cmo-to-coo.md`

```markdown
# CMO → COO Insights

**Purpose:** Content work reveals operations improvements. Log here for COO to implement.

---

## Template

```
## [Insight Name] (Logged: YYYY-MM-DD)

**Source:** [Post title or audience feedback]
**Insight:** [What audience needs/struggles with]
**COO application:** [How to improve operations]
**Status:** Pending / Implemented
```

---

## Logged Insights

<!-- Add new entries above this line -->
```

---

### 4. `memories/flywheel/complete-cycles.md`

```markdown
# Complete Flywheel Cycles

**Purpose:** Track end-to-end COO → CMO → Authority → Client cycles.

---

## Metrics to Track

| Metric | Target | Current |
|--------|--------|---------|
| COO → Content time | <7 days | TBD |
| Content engagement | 4%+ | TBD |
| Inquiries per month | 5+ | TBD |
| Complete cycles/month | 1+ | TBD |

---

## Template for New Cycle

```
## Cycle: [Name] (Started: YYYY-MM-DD)

### Timeline
- YYYY-MM-DD: COO implements [workflow]
- YYYY-MM-DD: Logged to content-opportunities.md
- YYYY-MM-DD: CMO publishes [free/paid] post
- YYYY-MM-DD: Post hits [X]% engagement
- YYYY-MM-DD: [N] client inquiries received
- YYYY-MM-DD: [N] inquiries convert to projects

### Metrics
- Time COO → Content: [N] days
- Engagement: [X]%
- Inquiry rate: [N] inquiries / [N] views
- Conversion: [N]/[N] inquiries

### Lessons
- [What worked]
- [What to improve]
```

---

## Completed Cycles

<!-- Add new cycles above this line -->
```

---

### 5. `memories/context-management/compaction-strategies.md`

```markdown
# Context Management Workflow

**When to use:** 60%+ context or before long tasks

---

## Steps

### 1. Assess Context Level

| Level | Action |
|-------|--------|
| 60-70% | Consider compaction |
| 70-80% | Run compaction |
| 80%+ | Immediate compaction |

### 2. Pre-Compact Checklist

- [ ] Note critical decisions made
- [ ] List current blockers
- [ ] Verify TodoWrite reflects progress
- [ ] Identify key file paths discovered
- [ ] List memory files used this session

### 3. What to Preserve

**Keep:**
- Decisions + rationale
- Blockers + status
- Progress state (done vs next)
- Key file paths
- Memory files referenced

**Discard:**
- Exploration details
- Search results
- Superseded plans
- Verbose outputs
- Completed task details (in memories/)

### 4. Context Reload Format

After compaction, note:
```
Memory files used:
- COO/memories/financial/budget-variance.md
- memories/domain-handoffs/content-opportunities.md

Load these on next session for instant context.
```

---

## Common Issues

| Problem | Solution |
|---------|----------|
| Waited until 95% | Set reminder at 60% |
| Lost key paths | Always note paths pre-compact |
| Forgot progress | Update TodoWrite before compact |
```

---

### 6. `memories/ceo-decisions/act-vs-ask.md`

```markdown
# Act vs Ask Decision Thresholds

**When to use:** Uncertain whether to act autonomously or ask CEO first.

---

## Act (No Approval Needed)

- File organization
- Status updates
- Draft generation
- Research and exploration
- Memory updates
- Internal documentation

---

## Ask First (Always)

- Anything involving money
- Client-facing communications
- External parties contact
- Irreversible actions
- Financial/contractual decisions
- Sending emails or messages

---

## Decision Framework

```
Is it reversible?
├── YES → Can likely act
└── NO → Ask first

Does it involve money?
├── YES → Always ask
└── NO → Continue evaluation

Is it client-facing?
├── YES → Draft first, CEO reviews
└── NO → Can likely act

Does it affect external parties?
├── YES → Ask first
└── NO → Can likely act
```

---

## When in Doubt

**Bias toward asking.** A 30-second clarification beats a 30-minute correction.
```

---

## CLAUDE.md Modification

**File:** `/Users/donovan/PROMAN_OS/CLAUDE.md`

**Insert after "Behavioral Defaults" section (~line 50), before "Mode Commands":**

```markdown
---

## Main Execution Loop (MANDATORY)

Before executing any multi-step task:

### Step 1: SEARCH MEMORIES
```bash
# Determine domain, then search:
grep -ri "[keyword]" memories/           # Cross-domain
grep -ri "[keyword]" COO/memories/       # Operations
grep -ri "[keyword]" CMO/memories/       # Content
```

If workflow found → READ IT COMPLETELY, use as written.

### Step 2: EXECUTE
- Follow existing workflow exactly if found
- If no workflow → Plan approach, note why no pattern exists

### Step 3: CAPTURE LEARNING
- New workflow created → Save to appropriate `memories/`
- Existing workflow had issues → Update it

**When to capture:** Multi-step processes (3+ steps), repeated patterns, cross-domain coordination, successful troubleshooting.

**When NOT to capture:** One-off tasks, simple 1-2 step operations, pure conversation.

---
```

---

## Implementation Checklist

- [ ] Create `memories/` directory
- [ ] Create `memories/domain-handoffs/` directory
- [ ] Create `memories/flywheel/` directory
- [ ] Create `memories/context-management/` directory
- [ ] Create `memories/ceo-decisions/` directory
- [ ] Create `memories/README.md`
- [ ] Create `memories/domain-handoffs/content-opportunities.md`
- [ ] Create `memories/domain-handoffs/cmo-to-coo.md`
- [ ] Create `memories/flywheel/complete-cycles.md`
- [ ] Create `memories/context-management/compaction-strategies.md`
- [ ] Create `memories/ceo-decisions/act-vs-ask.md`
- [ ] Modify `CLAUDE.md` with Main Execution Loop
