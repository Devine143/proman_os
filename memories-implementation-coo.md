# Phase 2: COO Memory System Implementation

**Location:** `/Users/donovan/PROMAN_OS/COO/memories/`

---

## Memory → Agent/Skill Promotion Pipeline

Memories are **workflow candidates**. Track usage, and promote to agents/skills when validated.

```
Document workflow → Use 5+ times → 80%+ success → Promote
```

### Tracking Fields (in every memory file)

```markdown
**When to use:** [Trigger conditions]
**Last used:** [Date]
**Use count:** [N] ← increment each use
**Success rate:** [High/Medium/Low]
**Promotion status:** Memory | Candidate | Promoted to @agent-name
```

### COO Promotion Examples

| Memory | After 5+ uses, promote to |
|--------|---------------------------|
| `loi-creation.md` | `@loi-generator` agent |
| `budget-variance.md` | `@budget-monitor` agent |
| `status-reports.md` | `skill:project-status` |
| `file-organization.md` | `@project-setup` agent |

### Monthly Review

Check `memories/` for promotion candidates:
```bash
grep -r "Use count:" memories/ | sort -t: -k2 -rn
```

---

## Directory Structure to Create

```
COO/memories/
├── README.md
├── procurement/
│   ├── loi-creation.md
│   ├── contractor-selection.md
│   └── negotiation-tactics.md
├── financial/
│   ├── budget-variance.md
│   └── cpi-spi-scenarios.md
├── client-communication/
│   ├── status-reports.md
│   └── difficult-conversations.md
└── project-documentation/
    └── file-organization.md
```

---

## Files to Create

### 1. `COO/memories/README.md`

```markdown
# COO Workflow Memory

Search here FIRST before any operations task.

## Quick Index

| Task Type | Search First |
|-----------|--------------|
| Create LOI | `procurement/loi-creation.md` |
| Select contractor | `procurement/contractor-selection.md` |
| Negotiate terms | `procurement/negotiation-tactics.md` |
| Budget analysis | `financial/budget-variance.md` |
| CPI/SPI review | `financial/cpi-spi-scenarios.md` |
| Status report | `client-communication/status-reports.md` |
| Difficult conversation | `client-communication/difficult-conversations.md` |
| File organization | `project-documentation/file-organization.md` |

## How to Search

```bash
# All COO memories
grep -ri "[keyword]" memories/

# By category
grep -ri "[keyword]" memories/procurement/
grep -ri "[keyword]" memories/financial/
grep -ri "[keyword]" memories/client-communication/
grep -ri "[keyword]" memories/project-documentation/
```

## Execution Loop (COO)

1. **SEARCH** - Check this folder before starting
2. **DECIDE** - Use existing workflow OR plan new
3. **EXECUTE** - Follow steps, use agents/commands
4. **CAPTURE** - Update memory with learnings
5. **FLYWHEEL CHECK** - "Could this become content?"
   - If YES → Log to `../memories/domain-handoffs/content-opportunities.md`

## Related Resources

- SOPs: `../sops/` (comprehensive procedures)
- Agents: @procurement-manager, @financial-controller, @client-relations
- Commands: /project-status, /budget-analysis, /loi
```

---

### 2. `COO/memories/procurement/loi-creation.md`

```markdown
# LOI Creation Workflow

**When to use:** Contractor approved but formal contract not yet executed
**Last used:** [Date]
**Success rate:** High

---

## Prerequisites

- [ ] Contractor quote received
- [ ] Scope clearly defined
- [ ] JBCC reference available
- [ ] Project structure exists
- [ ] Budget approved

---

## Steps

### 1. Gather Information (5-10 min)

Collect:
- Project name and location
- Tender reference and date
- Total tendered amount (excl VAT)
- Scope summary (2-3 sentences)
- Tentative site commencement date
- Performance guarantee % (typically 10%)

### 2. Generate LOI (10-15 min)

**Trigger:** "AI LOI for [Contractor Name]"
**Routes to:** @procurement-manager

Provide:
- Contractor name
- Scope description
- Contract value
- Key dates
- Special conditions (if any)

**Template location:** `templates/loi/standard-loi-template.docx`

### 3. Review Checklist (5-10 min)

- [ ] Conditional nature clearly stated
- [ ] Authorization scope limited (planning only, NOT physical works)
- [ ] Required documentation list with deadlines
- [ ] JBCC Edition 6.2 reference
- [ ] Performance guarantee terms (10% default)
- [ ] Payment terms aligned with tender

### 4. Finalize (5 min)

**Save to:** `projects/[project]/05-procurement/[Contractor]_LOI_[YYYYMMDD].docx`
**Update:** PROJECT_STATUS.md with LOI issuance
**CEO review:** Required if value >R50k

### 5. Distribute

- Email to contractor
- CC client if required by contract
- File signed copy when returned

---

## Edge Cases

### Early Site Access Required
Add clause: "Limited site access granted for [specific activities] subject to [conditions]"

### Value Over R5M
- Require CEO approval before issuance
- Additional review of payment terms
- Consider phased authorization

### Nominated vs Selected Subcontractor
- **Nominated:** Client-specified, include client approval acknowledgment
- **Selected:** Contractor choice, include tender evaluation reference

### Performance Guarantee Negotiation
- Standard: 10% of contract value
- Can reduce to 5% for established relationships
- Never below 5% (company policy)

---

## Tools/References

- **Agent:** @procurement-manager
- **Command:** /loi
- **Template:** `templates/loi/standard-loi-template.docx`
- **SOP:** `sops/sop-loi-management.md`

---

## Lessons Learned

**"NO physical works" clause:** Added after contractor misunderstood authorization scope. Now standard in all LOIs.

**Performance guarantee timing:** Due BEFORE Notice to Proceed, not after. Prevents mobilization delays.

**Documentation deadline:** Enforce strictly - if contractor doesn't submit insurance/CIDB within LOI timeframe, delay NTP.

---

## Content Opportunity

[If this workflow leads to content-worthy insight, log to `../../memories/domain-handoffs/content-opportunities.md`]
```

---

### 3. `COO/memories/procurement/contractor-selection.md`

```markdown
# Contractor Selection Workflow

**When to use:** Evaluating tender responses, selecting subcontractors
**Last used:** [Date]
**Success rate:** High

---

## Prerequisites

- [ ] Tender documents issued
- [ ] Minimum 3 responses received (or justified exception)
- [ ] Evaluation criteria defined
- [ ] Budget allocation confirmed

---

## Steps

### 1. Compile Responses

- Create comparison spreadsheet
- Normalize pricing (same scope assumptions)
- Verify all required documents submitted

### 2. Technical Evaluation

Score each contractor:
- [ ] Previous experience (similar projects)
- [ ] Team qualifications
- [ ] Methodology/approach
- [ ] Program compliance
- [ ] References checked

### 3. Commercial Evaluation

Compare:
- [ ] Total price
- [ ] Unit rates (for variations)
- [ ] Payment terms
- [ ] Exclusions and qualifications
- [ ] Risk allocation

### 4. Recommendation

**Format:**
```
Recommended: [Contractor Name]
Reason: [2-3 sentences]
Risk: [Key risk and mitigation]
Alternative: [Second choice and why not selected]
```

### 5. Approval and Award

- Present to CEO if >R100k
- Present to client if required
- Issue LOI (see `loi-creation.md`)

---

## Edge Cases

### Single Tender
- Document justification thoroughly
- Benchmark against market rates
- CEO approval required

### Price Significantly Below Others
- Investigate scope understanding
- Request clarification meeting
- Consider risk of variations

### Incumbent Contractor
- Evaluate fairly against others
- Document performance history
- Consider relationship value

---

## Tools/References

- **Agent:** @procurement-manager
- **Template:** `templates/tender-evaluation-matrix.xlsx`
- **SOP:** `sops/sop-consultant-selection-onboarding.md`

---

## Lessons Learned

[Add learnings from actual selections]
```

---

### 4. `COO/memories/procurement/negotiation-tactics.md`

```markdown
# Negotiation Tactics Workflow

**When to use:** Pre-contract negotiations, variation discussions, dispute resolution
**Last used:** [Date]
**Success rate:** Medium-High

---

## Prerequisites

- [ ] Clear understanding of own position
- [ ] BATNA identified (Best Alternative)
- [ ] Authority limits known
- [ ] Key issues prioritized

---

## Steps

### 1. Preparation (Before Meeting)

**Invoke:** @procurement-manager with "Prepare negotiation brief for [contractor/issue]"

Prepare:
- [ ] List of issues to negotiate
- [ ] Target outcome for each issue
- [ ] Walk-away point for each issue
- [ ] Concessions you can offer
- [ ] Contractor's likely position

### 2. Opening

- Start with areas of agreement
- State objectives clearly
- Listen to their position fully

### 3. Exploration

- Ask open questions
- Understand their constraints
- Identify creative solutions
- Look for trades (give X, get Y)

### 4. Bargaining

- Start with less important issues
- Build momentum with small wins
- Save difficult issues for when rapport established
- Document agreements as you go

### 5. Closing

- Summarize all agreements
- Confirm next steps
- Set deadlines for follow-up
- Document in meeting minutes

### 6. Post-Negotiation

**Invoke:** @procurement-manager with "Debrief negotiation with [contractor]"

- Send confirmation email within 24 hours
- Update contract documents
- Log lessons learned

---

## Edge Cases

### Deadlock
- Take a break
- Involve senior stakeholders
- Consider third-party mediation
- Revisit in writing

### Aggressive Tactics
- Stay calm, don't respond in kind
- Focus on interests, not positions
- Take breaks as needed
- Document inappropriate behavior

### Time Pressure
- Don't rush decisions
- Request extension if needed
- Be willing to walk away

---

## Tools/References

- **Agent:** @procurement-manager
- **SOP:** `sops/sop-contractor-negotiation-prep.md`
- **SOP:** `sops/sop-negotiation-debrief.md`

---

## Lessons Learned

[Add learnings from actual negotiations]
```

---

### 5. `COO/memories/financial/budget-variance.md`

```markdown
# Budget Variance Analysis Workflow

**When to use:** Monthly budget review, cost overrun investigation, client reporting
**Last used:** [Date]
**Success rate:** High

---

## Prerequisites

- [ ] Current cost data extracted
- [ ] Original budget baseline
- [ ] Approved variations list
- [ ] Commitment register updated

---

## Steps

### 1. Extract Current Costs

- Pull from accounting system
- Reconcile with invoices
- Include commitments (orders not yet invoiced)

### 2. Calculate Variances

**Command:** `/budget-analysis [project]`
**Agent:** @financial-controller

For each cost line:
```
Variance = Actual - Budget
Variance % = (Actual - Budget) / Budget × 100
```

### 3. Categorize Variances

| Category | Action |
|----------|--------|
| <5% | Note, no action |
| 5-10% | Investigate cause |
| >10% | Escalate, remedial action |

### 4. Root Cause Analysis

For significant variances (>5%):
- [ ] Scope change?
- [ ] Price increase?
- [ ] Quantity increase?
- [ ] Estimation error?
- [ ] External factor?

### 5. Forecast Impact

- Project final cost
- Identify recovery actions
- Update risk register

### 6. Report

**Include:**
- Summary table (budget vs actual vs forecast)
- Top 5 variances with explanations
- Recovery actions
- Forecast confidence level

**Save to:** `projects/[project]/03-financials/[YYYYMM]_Budget_Variance.xlsx`

---

## Edge Cases

### Positive Variance (Under Budget)
- Verify work complete (not just delayed)
- Check quality not compromised
- Consider reallocation to overspent areas

### Variation Claims Pending
- Show budget excluding disputed items
- Provide sensitivity analysis
- Note contingency position

### Multiple Currencies
- Use consistent exchange rate
- Show FX impact separately
- Update hedging if applicable

---

## Tools/References

- **Command:** /budget-analysis
- **Agent:** @financial-controller
- **SOP:** `sops/sop-budget-status-reporting.md`
- **Template:** `templates/budget-variance-template.xlsx`

---

## Lessons Learned

**Early detection critical:** Check weekly, not monthly. Small variances compound.

**Commitments matter:** Include POs issued but not invoiced. Avoids surprises.

**Context for client:** Always explain "why" - clients accept variances better when understood.

---

## Content Opportunity

Budget variance analysis with AI monitoring → Strong content angle for "The AI PM"
```

---

### 6. `COO/memories/financial/cpi-spi-scenarios.md`

```markdown
# CPI/SPI Analysis Workflow

**When to use:** Earned Value reporting, project health assessment, forecasting
**Last used:** [Date]
**Success rate:** High

---

## Prerequisites

- [ ] Work packages defined with % complete
- [ ] Planned Value (PV) baseline established
- [ ] Actual Cost (AC) data current
- [ ] Earned Value (EV) assessed

---

## Key Formulas

```
CPI = EV / AC    (Cost Performance Index)
SPI = EV / PV    (Schedule Performance Index)

EAC = BAC / CPI  (Estimate at Completion)
ETC = EAC - AC   (Estimate to Complete)
VAC = BAC - EAC  (Variance at Completion)
```

---

## Steps

### 1. Calculate Current Status

**Command:** `/budget-analysis [project]` (includes EVM metrics)

### 2. Interpret Results

| CPI | SPI | Status | Action |
|-----|-----|--------|--------|
| >1 | >1 | Under budget, ahead of schedule | Monitor, potential savings |
| >1 | <1 | Under budget, behind schedule | Accelerate with cost buffer |
| <1 | >1 | Over budget, ahead of schedule | Control costs, maintain schedule |
| <1 | <1 | Over budget, behind schedule | Urgent intervention required |

### 3. Trend Analysis

Plot CPI/SPI over time:
- Improving trend: Recovery likely
- Flat trend: Current trajectory
- Declining trend: Intervention needed

### 4. Forecast

```
EAC = AC + (BAC - EV) / CPI
Forecast completion = Today + (Remaining work / SPI rate)
```

### 5. Report

Include:
- Current CPI/SPI
- Trend chart (last 6 periods)
- EAC and forecast completion
- Variance explanations
- Recovery actions

---

## Common Scenarios

### CPI = 0.85 (15% over budget)

**Questions to ask:**
- Is this a one-time event or trend?
- What cost categories are driving it?
- Can scope be reduced?
- Is re-baseline appropriate?

### SPI = 0.75 (25% behind schedule)

**Questions to ask:**
- Is critical path affected?
- Can resources be added?
- Can scope be reduced or phased?
- What's the float situation?

### Both <1 (Red project)

**Immediate actions:**
1. Root cause analysis
2. Recovery plan within 48 hours
3. Client notification (CEO approval)
4. Weekly monitoring minimum

---

## Tools/References

- **Command:** /budget-analysis
- **Agent:** @financial-controller
- **SOP:** `sops/sop-budget-status-reporting.md`

---

## Lessons Learned

[Add learnings from actual EVM analysis]
```

---

### 7. `COO/memories/client-communication/status-reports.md`

```markdown
# Client Status Report Workflow

**When to use:** Weekly/monthly client updates, project reviews
**Last used:** [Date]
**Success rate:** High

---

## Prerequisites

- [ ] Progress data current
- [ ] Issues log updated
- [ ] Photos taken (if applicable)
- [ ] Financial summary ready

---

## Steps

### 1. Gather Inputs

**Trigger:** "AI Project Status for [project]"
**Routes to:** @client-relations

Collect:
- Overall % complete
- Key milestones status
- Issues/risks
- Lookahead (next period)
- Photos (if site-based)

### 2. Generate Report

**Command:** `/project-status [project]`

Standard sections:
1. Executive Summary (3 bullets max)
2. Progress vs Plan
3. Key Issues & Actions
4. Financial Summary (if contractually required)
5. Next Period Lookahead
6. Photos/Evidence (optional)

### 3. Review Checklist

- [ ] Tone appropriate (professional, constructive)
- [ ] Numbers accurate and consistent
- [ ] Issues framed with solutions
- [ ] No surprises (pre-communicate bad news)
- [ ] Attachments referenced correctly

### 4. CEO Review

**Required if:**
- Project in red status
- Financial variance >10%
- Contractual claim mentioned
- Scope change requested

### 5. Distribute

- Email to client contact list
- CC internal stakeholders
- File in `projects/[project]/07-communications/[YYYYMMDD]_Status_Report.pdf`

---

## Edge Cases

### Bad News Delivery
- Lead with facts, not opinions
- Provide context and root cause
- Present recovery plan
- Offer meeting to discuss

### Client Requests More Detail
- Provide supporting data
- Offer site visit
- Consider reporting frequency increase

### Milestone Slippage
- Be specific about impact
- Distinguish critical vs non-critical
- Show recovery actions
- Update forecast

---

## Tools/References

- **Command:** /project-status
- **Agent:** @client-relations
- **SOP:** `sops/sop-client-discovery-onboarding.md`

---

## Lessons Learned

**Pre-communicate bad news:** Never surprise client in written report. Call first.

**Keep consistent format:** Clients appreciate predictability. Use same template.

**Evidence matters:** Photos and data more credible than words alone.
```

---

### 8. `COO/memories/client-communication/difficult-conversations.md`

```markdown
# Difficult Conversations Workflow

**When to use:** Delivering bad news, addressing conflicts, managing expectations
**Last used:** [Date]
**Success rate:** Medium

---

## Prerequisites

- [ ] Facts gathered and verified
- [ ] Own position clear
- [ ] Desired outcome defined
- [ ] CEO briefed (if significant)

---

## Steps

### 1. Prepare

- Write down key points (3 max)
- Anticipate their reaction
- Prepare responses to likely questions
- Choose appropriate medium (call > email for difficult topics)

### 2. Open

- Be direct but respectful
- State purpose clearly: "I need to discuss [topic]"
- Don't bury the lead

### 3. Deliver

**Framework: Situation-Impact-Action**
- **Situation:** Here's what happened (facts only)
- **Impact:** Here's why it matters
- **Action:** Here's what we're doing / propose

### 4. Listen

- Let them respond fully
- Acknowledge their concerns
- Don't get defensive

### 5. Resolve

- Find common ground
- Agree on next steps
- Set follow-up date

### 6. Document

- Send follow-up email summarizing discussion
- Update risk register if applicable
- Note lessons learned

---

## Scenarios

### Cost Overrun Notification
```
"I need to discuss the project budget. We've identified a [X%] variance
in [area]. This is due to [cause]. We're implementing [actions] to
recover [Y%]. I wanted to discuss this with you before the monthly report."
```

### Schedule Delay
```
"I need to update you on the program. We're now forecasting [milestone]
for [date] instead of [original date]. The main driver is [cause].
Here's our recovery plan: [actions]. What questions do you have?"
```

### Quality Issue
```
"We've identified a quality issue with [element]. It doesn't meet
[standard]. We've already instructed [contractor] to rectify at no
additional cost. I wanted you to be aware before you see it on site."
```

---

## Tools/References

- **Agent:** @client-relations
- **CEO escalation:** Required for disputes, claims, significant delays

---

## Lessons Learned

**Call before email:** Voice conveys tone, allows questions, shows respect.

**Own the problem:** Even if not your fault, you're the messenger. Don't blame.

**Have a plan:** Never deliver problems without proposed solutions.
```

---

### 9. `COO/memories/project-documentation/file-organization.md`

```markdown
# File Organization Workflow

**When to use:** New project setup, file cleanup, handover preparation
**Last used:** [Date]
**Success rate:** High

---

## Standard 10-Level Hierarchy

```
projects/[project-name]/
├── 00-inbox/           # Unsorted incoming
├── 01-governance/      # Contracts, appointments, authorities
├── 02-planning/        # Programs, schedules, WBS
├── 03-financials/      # Budgets, cashflows, invoices
├── 04-design/          # Drawings, specifications, RFIs
├── 05-procurement/     # Tenders, LOIs, subcontracts
├── 06-site/            # Site instructions, diaries, photos
├── 07-communications/  # Meeting minutes, correspondence
├── 08-quality/         # Inspections, NCRs, handover
├── 09-closeout/        # Final accounts, lessons learned
└── PROJECT_STATUS.md   # Current status summary
```

---

## Steps

### New Project Setup

1. Create folder from template
2. Copy standard templates to appropriate folders
3. Set up PROJECT_STATUS.md
4. Brief team on structure

### Daily Filing (from 00-inbox)

1. Check 00-inbox for new items
2. Rename using convention: `[YYYYMMDD]_[Type]_[Description].[ext]`
3. Move to appropriate folder
4. Update PROJECT_STATUS.md if significant

### Weekly Cleanup

- [ ] Process all items in 00-inbox
- [ ] Verify no files in wrong locations
- [ ] Update PROJECT_STATUS.md
- [ ] Archive superseded documents

---

## Naming Convention

```
[YYYYMMDD]_[Type]_[Description].[ext]

Examples:
20251130_LOI_ABC_Electrical.docx
20251130_MIN_Client_Progress_Meeting.pdf
20251130_DWG_Structural_Rev_C.pdf
```

**Type codes:**
- LOI = Letter of Intent
- MIN = Meeting Minutes
- DWG = Drawing
- RPT = Report
- INV = Invoice
- CON = Contract
- COR = Correspondence

---

## Edge Cases

### Large Projects
Add sub-folders within categories:
```
05-procurement/
├── electrical/
├── mechanical/
└── civil/
```

### Shared Drives
- Same structure
- Add `_ARCHIVE` folders for old versions
- Never delete, always archive

### Multiple Versions
- Keep all versions
- Use `_v1`, `_v2` or `_RevA`, `_RevB` suffix
- Move superseded to `_ARCHIVE` within folder

---

## Tools/References

- **SOP:** `sops/sop-project-file-organization.md`
- **Template:** `templates/project-folder-template/`

---

## Lessons Learned

**00-inbox discipline:** Process daily. Backlog becomes unmanageable quickly.

**Consistent naming:** Saves hours when searching later. Enforce strictly.

**PROJECT_STATUS.md:** Keep updated. Single source of truth for project state.
```

---

## COO/CLAUDE.md Modification

**File:** `/Users/donovan/PROMAN_OS/COO/CLAUDE.md`

**Insert after "Quick Start" section (~line 18):**

```markdown
---

## Workflow Memory System

**Before operations tasks:**
1. Search `memories/README.md` for relevant workflow
2. If found → Follow documented steps exactly
3. If not found → Plan approach, mark for capture

**Task → Category mapping:**
| Task | Search First |
|------|--------------|
| Create LOI | `memories/procurement/loi-creation.md` |
| Select contractor | `memories/procurement/contractor-selection.md` |
| Negotiate terms | `memories/procurement/negotiation-tactics.md` |
| Budget analysis | `memories/financial/budget-variance.md` |
| CPI/SPI review | `memories/financial/cpi-spi-scenarios.md` |
| Status report | `memories/client-communication/status-reports.md` |
| Difficult conversation | `memories/client-communication/difficult-conversations.md` |
| File organization | `memories/project-documentation/file-organization.md` |

**After operations tasks:**
- Update memory with new edge cases or lessons learned
- **MANDATORY FLYWHEEL CHECK:** "Could this become newsletter content?"
- If YES → Log to `../memories/domain-handoffs/content-opportunities.md`

---
```

---

## Implementation Checklist

- [ ] Create `COO/memories/` directory
- [ ] Create `COO/memories/procurement/` directory
- [ ] Create `COO/memories/financial/` directory
- [ ] Create `COO/memories/client-communication/` directory
- [ ] Create `COO/memories/project-documentation/` directory
- [ ] Create `COO/memories/README.md`
- [ ] Create `COO/memories/procurement/loi-creation.md`
- [ ] Create `COO/memories/procurement/contractor-selection.md`
- [ ] Create `COO/memories/procurement/negotiation-tactics.md`
- [ ] Create `COO/memories/financial/budget-variance.md`
- [ ] Create `COO/memories/financial/cpi-spi-scenarios.md`
- [ ] Create `COO/memories/client-communication/status-reports.md`
- [ ] Create `COO/memories/client-communication/difficult-conversations.md`
- [ ] Create `COO/memories/project-documentation/file-organization.md`
- [ ] Modify `COO/CLAUDE.md` with Workflow Memory System section
