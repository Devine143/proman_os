# The AI Research Blueprint: Build Your Own Decision-Ready Report System

**The exact templates, checklists, and prompts I use to turn complex questions into structured reports.**

*This is the implementation guide for the Pyramid Principle + AI workflow described in the free post. If you haven't read that yet, start there for the "why" - this post is the "how."*

---

## The Moment This Clicked for Me

I was staring at a R500,000 decision with a one-week deadline.

My client had asked a seemingly simple question: "Should we import aluminium windows from China instead of buying locally?" What looked like a straightforward cost comparison turned into a maze of compliance requirements, shipping logistics, supplier verification, and risk factors I hadn't even considered.

The old me would have done one of three things: spent R25,000 on consultants I couldn't afford, spent 20+ hours drowning in scattered research tabs, or—worst option—made the call with incomplete information and hoped for the best.

Instead, I sat down with Claude, a blank document, and a framework I'd been refining for months. Three hours later, I had a 30-page decision-ready report that covered regulatory compliance, landed costs, supplier evaluation, risk assessment, and clear go/no-go criteria for different scenarios.

The report didn't just answer the question. It gave my client a *system* for thinking about the decision—one they could apply to future projects without me.

That's what I'm giving you today. Not just templates, but a thinking system that compounds.

---

## The Economics (With Honest Caveats)

Before we dive into the templates, let me show you the real numbers—because this only works if you understand both the value and the limits.

**Traditional approach** for my aluminium import question:
- Hiring a generalist consultant: R15,000-R25,000
- Or: 15-20 hours of ad-hoc research (scattered, unstructured)
- Or: Making the decision with incomplete information (risky)

**AI-enhanced Pyramid Principle approach:**
- Your time: 2-3 hours (once you've internalized the method—see realistic estimates below)
- AI tools: R0-R400/month (Claude Pro or similar)
- Deliverable quality: Strong research foundation, not professional advice
- **Total: Your hourly rate × 3 hours**

**Important distinction:** This method replaces **research legwork**, not **professional judgment**. You're not asking AI to be a customs broker with 20 years of relationships and liability insurance. You're asking it to find and synthesize the same *information* that forms the basis of informed decisions.

The real value? You arrive at expert conversations 10x more prepared. When you do need a professional—and sometimes you will—you ask better questions, recognize gaps faster, and don't pay R800/hour for them to explain basics.

**Realistic expectations:**
- First project using this system: 6-8 hours (learning curve is real)
- Second project: 4-5 hours (methodology starts clicking)
- Ongoing: 2-3 hours (once it's internalized)

One comprehensive research report using this method saved me roughly R15,000 in consultant fees on the aluminium import analysis—and more importantly, gave me confidence in a decision I'd otherwise have made with incomplete information.

---

## Where I Got It Wrong (And What I Learned)

Before I give you the templates, you deserve to know where this method failed me—so you don't repeat my mistakes.

**The ITAC Permit Mistake**

In an early version of the aluminium import research, Claude confidently stated that ITAC (International Trade Administration Commission) import permits weren't required for aluminium window frames. The response was specific, well-structured, and completely wrong for certain HS codes.

I discovered this only because I made a 20-minute phone call to a clearing agent as a sanity check. She immediately flagged it: "That depends on the HS code classification. For some aluminium products, you absolutely need ITAC approval, and it takes 6-8 weeks."

Had I skipped that call and relied solely on AI research, I would have ordered products that would sit in customs for two months—destroying the project timeline and any cost savings.

**The Lesson:** AI is confident even when wrong. Regulatory requirements are exactly the domain where AI training data goes stale fastest. The "phone call test" in my validation checklist exists because of this failure.

**The Pricing Hallucination**

Another early project: AI gave me specific shipping rates from Foshan to Cape Town. The numbers were plausible, formatted beautifully in a table, and completely fabricated. When I requested quotes from actual freight forwarders, the real rates were 40% higher.

AI doesn't know current market rates. It knows *historical patterns* of what rates looked like in its training data. For anything price-sensitive, treat AI output as "directionally useful" not "quotable."

**What This Means for You**

These templates work. The methodology is sound. But AI research is a *starting point* for decisions, not an endpoint. The validation steps I include aren't optional—they're what separate "useful research" from "expensive mistakes."

---

## What You're Getting

In the free post, I showed you the transformation—messy question to decision-ready report. Now I'm giving you the exact machinery that makes it work.

Here's what's in this blueprint:

1. **The SCQA Template** - Fill-in-the-blank problem framing (the foundation everything else builds on)
2. **The MECE Checklist** - Ensure your research categories are airtight
3. **The Model Selection Guide** - Which AI to use for which task (this matters more than most people realize)
4. **The Research Prompt Library** - Copy-paste prompts with exact formatting that AI actually follows
5. **The Report Assembly Framework** - Structure your output so stakeholders can make decisions
6. **The Quality Validation Checklist** - Catch gaps before delivery (including the external verification steps that saved me from expensive mistakes)
7. **The Quick-Start Workflow** - Complete process on one page for when you just need to execute
8. **Advanced Techniques** - Risk registers, non-obvious insights, scenario frameworks for when "good enough" isn't good enough

Fair warning: this is a long post. But every section is designed to be used, not just read. Save it. Bookmark it. Come back when you have a real research project.

Let's build your system.

---

## Part 1: The SCQA Template

Before you touch AI, frame your research question using this template.

### The Fill-In Template

```markdown
## Research Brief: [Topic Name]

### SITUATION
Current state that everyone agrees on:
- Context: ________________________________
- Stakeholder: ________________________________
- Constraints: ________________________________
- Timeline: ________________________________

### COMPLICATION
What changed or what's the problem:
- The trigger: ________________________________
- Why it matters: ________________________________
- What's at stake: ________________________________

### QUESTION
The specific question(s) to answer:
- Primary question: ________________________________
- Secondary questions:
  1. ________________________________
  2. ________________________________
  3. ________________________________

### HYPOTHESIS (Your best guess at the answer)
- Initial recommendation: ________________________________
- Key assumptions to test:
  1. ________________________________
  2. ________________________________
  3. ________________________________
- What would change my mind: ________________________________
```

### Example: Aluminium Import Research

```markdown
## Research Brief: China Aluminium Import Feasibility

### SITUATION
- Context: Specifying windows/doors for large residential project in Cape Town
- Stakeholder: Property developer (cost-conscious, quality-aware)
- Constraints: Budget pressure, 6+ month timeline available
- Timeline: Decision needed within 1 week

### COMPLICATION
- The trigger: Client asked if Chinese imports could reduce costs
- Why it matters: 30-50% potential savings on R500k+ fenestration budget
- What's at stake: Cost savings vs. quality risk, compliance complexity

### QUESTION
- Primary: Should we import from China or buy locally?
- Secondary:
  1. What are the true landed costs (not just FOB)?
  2. What regulatory requirements apply?
  3. What risks exist and how do we mitigate them?

### HYPOTHESIS
- Initial recommendation: Import for large orders (>100m²) with long lead times
- Assumptions to test:
  1. Chinese quality can meet SA standards
  2. Landed cost savings are meaningful (>15%)
  3. Regulatory compliance is achievable
- What would change my mind: If landed costs are within 10% of local,
  or if compliance requirements add >3 months to timeline
```

**Why This Works:** You've transformed a vague question into a testable hypothesis with clear success criteria. Now AI has something specific to work with.

Most people skip this step. They jump straight into prompts, get scattered results, and blame the AI. The problem isn't the AI—it's the input. SCQA gives AI the clarity it needs to give you useful output.

---

## Part 2: The MECE Category Builder

You have a clear question. Now you need clear buckets to organize your research.

MECE stands for "Mutually Exclusive, Collectively Exhaustive." In plain English: your categories shouldn't overlap, and together they should cover everything relevant to your question.

I know—it sounds like consultant jargon. But once you internalize it, you'll spot research gaps you used to miss entirely.

### MECE Validation Checklist

For each category, ask yourself:

| Check | Question | Pass/Fail |
|-------|----------|-----------|
| **Mutual Exclusivity** | If I removed this category, would another category cover the same ground? | Should be NO |
| **Collective Exhaustion** | After all categories, could someone say "but what about X?" | Should be NO |
| **Direct Support** | Does this category directly help answer the primary question? | Should be YES |

### Common MECE Structures

**By Decision Factor:**
```
1. Cost analysis
2. Timeline/feasibility
3. Quality/risk
4. Compliance/regulatory
5. Recommendation/decision framework
```

**By Stakeholder:**
```
1. Client perspective
2. Supplier perspective
3. Regulatory perspective
4. End-user perspective
```

**By Time:**
```
1. Current state analysis
2. Implementation requirements
3. Ongoing maintenance/support
```

**By Process Phase:**
```
1. Pre-decision research
2. Selection/procurement
3. Implementation/delivery
4. Post-delivery support
```

### Example: Aluminium Import Categories

```markdown
## MECE Research Categories

1. **Regulatory Compliance**
   - Applicable standards (SANS)
   - Import permits (NRCS, ITAC)
   - Compliance timeline and process

2. **Landed Cost Analysis**
   - FOB pricing from China
   - Shipping and logistics costs
   - Import duties and VAT
   - Total landed cost comparison

3. **Supplier Evaluation**
   - Certification requirements
   - Capacity and track record
   - Communication and reliability

4. **Logistics & Timeline**
   - Manufacturing lead times
   - Shipping routes and duration
   - Customs clearance process

5. **Risk Assessment**
   - Quality risks and mitigation
   - Financial risks (FX, payment)
   - Operational risks (delays, compliance)

6. **Decision Framework**
   - Go/no-go criteria
   - Scenario recommendations
   - Implementation checklist

### MECE Validation:
- [ ] No category overlaps with another
- [ ] All aspects of the question are covered
- [ ] Each category directly informs the recommendation
```

Here's the breakthrough that took me months to internalize: **the quality of your categories determines the quality of your research.** Get the buckets wrong, and you'll either miss critical factors or waste time on overlapping analysis. Get them right, and AI becomes remarkably effective at filling each one.

---

## Part 3: The Research Prompt Library

Now the fun part. You have structure—clear question, clear categories. Here are the prompts to fill each bucket.

But first—which AI should you use?

### Choosing the Right Model for Research Tasks

We're past the era of "best model." Each AI optimizes for different things, and using the wrong one for your task means fighting against its design rather than leveraging its strengths.

**The core insight:** Each model takes a different stance toward messy information.

| Model | Core Question It Asks | Strength | Weakness |
|-------|----------------------|----------|----------|
| **Gemini** | "What's the story here? What does this mean?" | Finding insights in chaotic data, unexpected angles | Can produce outputs that contradict themselves |
| **Claude** | "What's actually there? How do I stay accurate?" | Maintaining consistency across outputs, flagging uncertainty | Can be too conservative when you want creative divergence |
| **ChatGPT** | "What structure should this follow?" | Deep logical reasoning on clean problems | Struggles with genuine ambiguity—invents structure rather than tolerating mess |

**For this research methodology, here's when to use each:**

**Use Gemini when:**
- You have massive, messy documents that need synthesis in a single shot (annual reports, research corpora, competitive analysis)
- You want to be surprised—you need unexpected angles or creative directions
- You're doing the initial "what's out there?" exploration phase
- The task rewards interpretation over precision

**Use ChatGPT when:**
- You have a clean, well-defined technical problem with unambiguous inputs
- You need deep architectural reasoning or system design
- Requirements are crystal clear and you need the logically correct answer
- You're building decision trees or structured frameworks

**Use Claude when:**
- You need coherent output across multiple rounds of editing (most of this methodology)
- The work involves iterative refinement where consistency matters
- You're processing messy operational data but need outputs that don't contradict themselves
- You want a model that flags uncertainty instead of inventing confidence

**The multi-model workflow I actually use:**

For comprehensive research projects, I often sequence models:

1. **Gemini first** - Initial massive synthesis, finding strategic angles I hadn't considered
2. **Claude for the core work** - Running the structured prompts, iterative refinement, maintaining coherence
3. **ChatGPT for specific technical questions** - When I need rigorous logical structure on a clean sub-problem
4. **Gemini again** - Final narrative polish, checking if I missed any angles

**The practical reality:** Most of these prompts work well with any capable model (Claude Pro, GPT-4, Gemini Advanced). But if you're getting inconsistent outputs or the AI keeps "improving" your structure in ways you didn't ask for, try switching models. The stance mismatch is often the problem.

---

**Critical difference from generic prompts:** These include exact output formatting. AI is much better at following specific structures than figuring out how to organize information. Tell it exactly what table format, what headings, what level of detail you need.

### Prompt Template: Category Research

```
I'm researching [TOPIC] to answer this question: [PRIMARY QUESTION]

Focus area: [SPECIFIC CATEGORY]

Context:
- [RELEVANT CONTEXT FROM SCQA]

Please provide your findings using this EXACT structure:

## [Category Name] Analysis

### Key Findings
| Finding | Implication | Confidence |
|---------|-------------|------------|
| [Finding 1] | [What it means for decision] | High/Medium/Low |
| [Finding 2] | [What it means for decision] | High/Medium/Low |

### Detailed Analysis
[Organized by sub-topic with specific data points]

### Risks & Considerations
- [Risk 1]: [Mitigation approach]
- [Risk 2]: [Mitigation approach]

### Impact on Recommendation
[2-3 sentences on how this affects the overall decision]

Keep the focus narrow - only cover [CATEGORY], not other aspects.
```

### Example Prompts Used for Aluminium Research

**Prompt 1: Regulatory Compliance**
```
I'm researching importing aluminium windows and doors from China to South Africa.

Focus area: Regulatory compliance and import requirements

Context:
- Product: Aluminium window and door systems
- Destination: South Africa (Cape Town)
- Use: Residential construction project

Please provide your findings using this EXACT structure:

## Regulatory Compliance Analysis

### Applicable Standards Summary
| Standard | Requirement | Mandatory? | Verification Method |
|----------|-------------|------------|---------------------|
| [SANS number] | [What it covers] | Yes/No | [How to prove compliance] |

### NRCS Letter of Authority
- **What it is:** [Description]
- **When required:** [Triggers]
- **Application process:** [Step-by-step]
- **Timeline:** [Expected duration]
- **Cost:** [If applicable]
- **Consequences of non-compliance:** [Penalties/risks]

### Import Permit Requirements
| Permit/Document | Issuing Body | Lead Time | Cost |
|-----------------|--------------|-----------|------|
| [Document] | [Authority] | [Days/weeks] | [Amount] |

### HS Codes and Duty Classification
- **Primary HS code:** [Code and description]
- **Duty rate:** [Percentage]
- **Special provisions:** [Any exemptions or additional requirements]

### Compliance Roadmap
| Step | Action | Timeline | Owner |
|------|--------|----------|-------|
| 1 | [Action] | [When] | [Who does this] |

Include specific standard numbers (e.g., SANS 613, SANS 10400-N) and
regulatory body contact details where available.
```

**Prompt 2: Landed Cost Analysis**

*Quick glossary if these terms are unfamiliar:*
- **FOB (Free On Board):** Price at the Chinese port before shipping—you pay everything after this point
- **CIF (Cost, Insurance, Freight):** Price including shipping and insurance to the destination port
- **HS Code:** Harmonized System code—the international classification number that determines your import duty rate
- **Landed Cost:** The total cost to get goods from factory to your door, including all taxes, shipping, and fees

```
I'm researching importing aluminium windows and doors from China to South Africa.

Focus area: Complete landed cost analysis

Context:
- Order size: ~100m² of sliding doors and windows
- Origin: China (Foshan manufacturing region)
- Destination: Cape Town, South Africa
- Current exchange rate: ~R18.20/USD

Please create a complete cost model using this EXACT structure:

## Landed Cost Analysis

### Cost Component Breakdown
| Cost Item | Amount (USD) | Amount (ZAR) | % of Total | Notes |
|-----------|--------------|--------------|------------|-------|
| FOB Price (per m²) | | | | Range: low-high |
| Sea Freight (40ft) | | | | Current rates |
| Import Duty | | | | HS 7610.10 rate |
| VAT (15%) | | | | On CIF + duty |
| Clearing & Forwarding | | | | Typical range |
| Local Transport (to CPT) | | | | Estimate |
| Contingency (5%) | | | | Buffer |
| **Total Landed per m²** | | | 100% | |

### Comparison with Local Pricing
| Metric | Chinese Import | SA Local | Difference |
|--------|----------------|----------|------------|
| Price per m² | R_____ | R_____ | ___% |
| Lead time | ___weeks | ___weeks | ___weeks |
| Warranty | [Terms] | [Terms] | [Comparison] |
| After-sales support | [Rating] | [Rating] | [Notes] |

### Break-Even Analysis
- **Minimum order size for savings:** ___m²
- **Break-even at:** R___/USD exchange rate
- **Savings potential at 100m²:** R_____

### Sensitivity Analysis
| Variable | Base Case | -20% | +20% | Impact on Decision |
|----------|-----------|------|------|-------------------|
| Exchange rate | R18.20 | R14.56 | R21.84 | [Effect] |
| Freight cost | $_____ | $_____ | $_____ | [Effect] |
| FOB price | $_____ | $_____ | $_____ | [Effect] |

Use current market rates. Flag any figures that may be volatile.
```

**Prompt 3: Supplier Evaluation**
```
I'm researching Chinese manufacturers of aluminium windows and doors
for export to South Africa.

Focus area: Supplier identification and evaluation

Please provide using this EXACT structure:

## Supplier Evaluation Framework

### Top Manufacturers Overview
| Company | Location | Certifications | Capacity | MOQ | Africa Experience |
|---------|----------|----------------|----------|-----|-------------------|
| [Name] | [City] | ISO/CE/etc | [m²/year] | [m²] | Yes/No + details |

### Certification Priority Matrix
| Certification | Importance | Why It Matters | How to Verify |
|---------------|------------|----------------|---------------|
| [Cert] | Critical/Important/Nice-to-have | [Reason] | [Method] |

### Red Flags Checklist
- [ ] [Red flag 1] - What to look for: [Details]
- [ ] [Red flag 2] - What to look for: [Details]
- [ ] [Red flag 3] - What to look for: [Details]

### Due Diligence Checklist
| Step | Action | Timing | Cost | Notes |
|------|--------|--------|------|-------|
| 1 | [Action] | Before/During/After order | Free/Paid | [Details] |

### Supplier Verification Methods
| Method | Cost | Reliability | Timeline |
|--------|------|-------------|----------|
| Desktop research | Free | Low-Medium | 1-2 hours |
| Video factory tour | Free | Medium | 1 hour |
| Third-party audit | $___-$___ | High | ___weeks |
| Sample order | $___-$___ | High | ___weeks |

### Sample & Testing Protocol
1. **Initial sample:** [What to request, quantity, cost]
2. **Testing requirements:** [Which tests, where to conduct]
3. **Approval criteria:** [Pass/fail thresholds]
```

**Prompt 4: Risk Assessment (Professional Risk Register)**
```
I'm researching importing aluminium windows from China to South Africa.

Focus area: Comprehensive risk assessment and mitigation

Context:
- First-time import (no established supplier relationship)
- Budget-sensitive project (cost savings are the driver)
- Quality is important (residential end-use)

Please create a professional risk register using this EXACT structure:

## Risk Assessment

### Risk Register
| ID | Risk Category | Risk Description | Likelihood | Impact | Risk Score | Mitigation Strategy | Residual Risk | Owner |
|----|---------------|------------------|------------|--------|------------|---------------------|---------------|-------|
| R1 | Quality | [Specific risk] | H/M/L | H/M/L | [L×I] | [Specific action] | H/M/L | [Role] |
| R2 | Compliance | [Specific risk] | H/M/L | H/M/L | [L×I] | [Specific action] | H/M/L | [Role] |
| R3 | Financial | [Specific risk] | H/M/L | H/M/L | [L×I] | [Specific action] | H/M/L | [Role] |
| R4 | Logistics | [Specific risk] | H/M/L | H/M/L | [L×I] | [Specific action] | H/M/L | [Role] |
| R5 | Relationship | [Specific risk] | H/M/L | H/M/L | [L×I] | [Specific action] | H/M/L | [Role] |

### Risk Categories to Assess
1. **Quality/Specification** - Product doesn't meet standards, poor workmanship
2. **Regulatory/Compliance** - Customs rejection, NRCS failure, certification issues
3. **Financial** - FX movement, payment fraud, hidden costs
4. **Logistics** - Shipping delays, damage in transit, customs holdups
5. **Relationship** - Communication breakdown, warranty disputes, supplier default

### Risk Scoring Matrix
|  | Low Impact | Medium Impact | High Impact |
|--|------------|---------------|-------------|
| **High Likelihood** | Medium | High | Critical |
| **Medium Likelihood** | Low | Medium | High |
| **Low Likelihood** | Low | Low | Medium |

### Mitigation Implementation Checklist
| Risk ID | Mitigation Action | Timing | Cost | Status |
|---------|-------------------|--------|------|--------|
| R1 | [Action] | Pre-order | R___ | [ ] |
| R2 | [Action] | Pre-order | R___ | [ ] |

### Contingency Plans
For each HIGH or CRITICAL risk, provide:
- **Trigger:** What signals this risk is materializing
- **Response:** Immediate actions to take
- **Escalation:** Who to involve and when
```

### Prompt: Synthesize Into Decision Framework

After gathering category research, use this prompt:

```
I've completed research on [TOPIC] across these categories:
1. [Category 1 - key findings summary]
2. [Category 2 - key findings summary]
3. [Category 3 - key findings summary]
4. [Category 4 - key findings summary]

Original question: [PRIMARY QUESTION]
Original hypothesis: [YOUR HYPOTHESIS]

Please help me:
1. Validate or revise my hypothesis based on the findings
2. Create a decision framework with clear criteria
3. Develop scenario-based recommendations (when to do X vs Y)
4. Identify the key decision points and thresholds
5. Create a visual decision tree if applicable

The output should enable someone to make a confident decision
without reading all the underlying research.
```

At this point, you've got raw material—structured, yes, but still scattered across multiple AI conversations. The next step transforms that raw material into something you can actually hand to a stakeholder.

---

## Part 4: The Report Assembly Framework

This is where the Pyramid Principle earns its name. You're taking all that research and structuring it so the most important thing comes first—and every supporting detail flows logically beneath it.

### Report Template

```markdown
# [Report Title]: [Topic] Analysis

**Research Date:** [Date]
**Prepared For:** [Stakeholder]
**Classification:** [Decision Support / Information Only / etc.]

---

## 1. Executive Summary

### Key Findings
1. [Most important finding - one sentence]
2. [Second most important finding]
3. [Third finding]
4. [Fourth finding if needed]

### Recommendation
[Clear, actionable recommendation in 2-3 sentences]

### Go/No-Go Summary
| Scenario | Recommendation |
|----------|----------------|
| [Scenario A] | GO / NO-GO / CONDITIONAL |
| [Scenario B] | GO / NO-GO / CONDITIONAL |
| [Scenario C] | GO / NO-GO / CONDITIONAL |

---

## 2. [Category 1 Title]

### 2.1 [Sub-topic]
[Content]

### 2.2 [Sub-topic]
[Content]

---

## 3. [Category 2 Title]
[Same structure]

---

## [N]. Decision Framework

### When to [Option A]
| Factor | Threshold |
|--------|-----------|
| [Factor 1] | [Specific criteria] |
| [Factor 2] | [Specific criteria] |

### When to [Option B]
[Same structure]

### Decision Tree
```
[Visual decision flow]
```

---

## [N+1]. Recommendations

### Recommended Approach
[Specific recommendation with reasoning]

### Implementation Checklist
- [ ] [Step 1]
- [ ] [Step 2]
- [ ] [Step 3]

### Next Steps
| Priority | Action | Owner | Timeline |
|----------|--------|-------|----------|
| Immediate | [Action] | [Who] | This week |
| Short-term | [Action] | [Who] | 2-4 weeks |
| Medium-term | [Action] | [Who] | 1-3 months |

---

## [N+2]. Non-Obvious Insights

### [Insight 1 Name]: [Headline]
**What it means:** [Explanation]
**Why it matters:** [Strategic implication]

### [Insight 2 Name]: [Headline]
**What it means:** [Explanation]
**Why it matters:** [Strategic implication]

---

## Appendices

### A. Compliance/Regulatory Checklist
| Requirement | Standard/Authority | Evidence Required | Status |
|-------------|--------------------|-------------------|--------|
| [Req 1] | [Standard] | [Document] | [ ] |

### B. Detailed Cost Calculations
| Line Item | Amount | Assumptions | Source |
|-----------|--------|-------------|--------|
| [Item] | R_____ | [Key assumption] | [Where from] |

### C. Risk Register (Complete)
| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|----|------|------------|--------|------------|-------|
| R1 | [Risk] | H/M/L | H/M/L | [Action] | [Role] |

### D. Supplier/Vendor Evaluation Matrix
| Criteria | Weight | Supplier A | Supplier B | Supplier C |
|----------|--------|------------|------------|------------|
| [Criterion] | X% | [Score] | [Score] | [Score] |

### E. Source Citations
| Finding | Source | Date Accessed | Reliability |
|---------|--------|---------------|-------------|
| [Key claim] | [URL/Document] | [Date] | High/Medium/Low |
```

You've now got a complete report. But here's where most people make a critical mistake: they deliver it without validation. And that's how expensive errors slip through.

---

## Part 5: Quality Validation Checklist

This is the section I wish someone had given me before my first AI-assisted research project. It would have saved me from the ITAC permit mistake I mentioned earlier.

Before delivering, validate with this checklist. **Critical note:** AI checking AI is like asking the person who made a mistake to review their own work. The validation process below includes both AI review *and* external verification steps.

### Structure Validation

- [ ] **Main message is first** - Could someone read only the executive summary and know what to do?
- [ ] **Arguments are MECE** - No overlaps, no gaps in categories
- [ ] **Evidence supports arguments** - Each claim has data behind it
- [ ] **Action is clear** - Reader knows exactly what to do next

### Content Validation

- [ ] **Sources cited** - Key data points have attribution
- [ ] **Numbers verified** - Calculations are correct, exchange rates current
- [ ] **Assumptions stated** - Reader knows what could change the recommendation
- [ ] **Risks acknowledged** - Downsides and uncertainties are addressed

### Decision-Readiness Validation

- [ ] **Scenarios covered** - Different situations have different recommendations
- [ ] **Thresholds defined** - Clear criteria for go/no-go decisions
- [ ] **Next steps actionable** - Reader can immediately take action
- [ ] **Timeline realistic** - Recommendations account for real-world constraints

### External Verification (Non-Negotiable)

AI research requires human validation. Don't skip these:

- [ ] **Primary source check** - Verify 3-5 critical facts against official sources (.gov.za websites, official regulations, published rate cards)
- [ ] **The phone call test** - Call one relevant authority to validate a key assumption (30 minutes with a clearing agent costs R0 and could save R50,000 in mistakes)
- [ ] **Recency check** - Confirm pricing, exchange rates, and regulatory requirements are current (AI training data has cutoff dates)
- [ ] **Domain expert spot-check** - If possible, have someone with relevant experience review the key findings (even a 15-minute conversation)

### AI Output Validation (Secondary, Not Primary)

Use this *after* external verification, not instead of it:

```
Review this research output for quality issues:

[PASTE YOUR DRAFT]

Check for:
1. Internal consistency - do different sections contradict each other?
2. Logical gaps - any arguments that don't connect?
3. Missing perspectives - any stakeholders or factors not considered?
4. Hedging language - where does the AI seem uncertain? (Flag these for external verification)
5. Specificity test - are numbers precise or vague? (Vague = needs verification)

Provide specific suggestions for improvement.
```

### Red Flags That Require Professional Help

Stop and consult an expert if:
- [ ] AI gives contradictory information when you rephrase the question
- [ ] Regulatory requirements seem unclear or have recent changes
- [ ] Financial stakes exceed R500,000
- [ ] Legal liability or compliance penalties are involved
- [ ] The decision requires physical verification (product quality, site conditions)
- [ ] You're operating in a domain where you can't evaluate whether the AI output is reasonable

That checklist might seem like overkill. It's not. The 30 minutes you spend on validation can save you from the kind of mistakes that destroy credibility—and cost real money.

---

## Part 6: Quick-Start Workflow

If the previous sections felt overwhelming, this is your cheat sheet. Print this page. Tape it to your wall. Use it until the process becomes automatic.

Here's the complete workflow in one page:

### Phase 1: Frame (15-20 minutes)
1. Complete SCQA template
2. Define MECE categories (3-6)
3. Validate categories with checklist

### Phase 2: Research (60-90 minutes)
1. Run category research prompts (one per category)
2. Capture key findings in category buckets
3. Note questions or gaps for follow-up

### Phase 3: Synthesize (20-30 minutes)
1. Run decision framework synthesis prompt
2. Validate/revise original hypothesis
3. Define scenarios and thresholds

### Phase 4: Assemble (30-45 minutes)
1. Use report template structure
2. Write executive summary LAST (after you know the answer)
3. Add appendices for supporting detail

### Phase 5: Validate (30-60 minutes)
1. Run structure and content validation checklists
2. **External verification** - verify 3-5 critical facts against primary sources
3. **Phone call test** - call one relevant authority on a key assumption
4. Run AI validation prompt (secondary, not primary)
5. Final read-through for clarity

**Total time for experienced users: 2.5-4 hours for a comprehensive research report**
**Total time for first project: 6-8 hours (learning curve is real—give yourself grace)**

That's the core system. For most projects, Parts 1-6 are everything you need.

But if you want to go from "solid report" to "this person really knows what they're doing"—the kind of work that makes stakeholders think differently about you—keep reading.

---

## Part 7: Advanced Techniques That Separate Good from Great

The templates above will get you 80% of the way to a professional report. These advanced techniques take you from "solid analysis" to "this person really knows what they're doing."

I discovered these through trial and error—here's what moves a report from informative to truly decision-ready.

### Technique 1: The Non-Obvious Insights Section

After you've completed your category research, most people stop. But the highest-value insights often emerge from patterns *across* categories, not within them.

**The Prompt:**
```
I've completed comprehensive research on [TOPIC]. Here's a summary of my findings:

Category 1 - [Key findings]:
[Summary]

Category 2 - [Key findings]:
[Summary]

Category 3 - [Key findings]:
[Summary]

[Continue for all categories]

Now step back and identify 3-5 "non-obvious insights" - patterns, thresholds,
paradoxes, or strategic implications that aren't immediately apparent from
any single category but emerge from the full picture.

Format each as:
### [Insight Name]: [One-sentence headline]
**What it means:** [2-3 sentence explanation]
**Why it matters:** [Strategic implication for the decision]
**Decision impact:** [How this changes the recommendation]
```

**Example from my Aluminium Import Research:**

Here's what this produced when I ran it on my actual findings:

> ### The Threshold Effect: Import economics are binary, not gradual
> **What it means:** Below ~50m², import costs per unit increase dramatically due to fixed costs (shipping, compliance, supplier setup) being spread across fewer units. Above 100m², unit economics become highly favorable. There's no smooth gradient—it's a step function.
> **Why it matters:** This reframes the decision from "should we import?" to "do we have enough volume to make importing viable?"
> **Decision impact:** Small projects should never import. Large projects should almost always consider it. The question isn't cost savings—it's order aggregation capability.

> ### The False Dichotomy Trap: Import vs Local isn't the real choice
> **What it means:** The research revealed a third option most people miss: establishing a relationship with a Chinese supplier for future projects while sourcing locally for this one. The compliance groundwork (NRCS approval, supplier vetting) has value beyond a single project.
> **Why it matters:** This changes the investment calculation—compliance costs are amortized across all future imports, not just this project.
> **Decision impact:** Even if the numbers don't work for this project, initiating the compliance process might still make sense for pipeline projects.

This section often becomes the most-referenced part of my reports. It's where the "so what?" lives.

---

### Technique 2: Scenario-Based Decision Frameworks

Don't give one recommendation. Give a framework that maps different situations to different actions.

**The Prompt:**
```
Based on my research on [TOPIC], create a scenario-based decision framework.

The key variables that affect the decision are:
1. [Variable 1, e.g., order size]
2. [Variable 2, e.g., timeline]
3. [Variable 3, e.g., risk tolerance]

Create a decision matrix that shows:
- What combination of variables leads to each recommendation
- Clear thresholds for each variable
- The logic behind each path

Format as:

## Decision Framework: [Topic]

### Key Decision Variables
| Variable | Low | Medium | High |
|----------|-----|--------|------|
| [Variable 1] | [Definition] | [Definition] | [Definition] |

### Scenario Matrix
| Scenario | Variable 1 | Variable 2 | Variable 3 | Recommendation | Rationale |
|----------|------------|------------|------------|----------------|-----------|

### Decision Tree
[Text-based flowchart showing the decision logic]
```

**Example Output from my Research:**

| Scenario | Order Size | Timeline | Risk Tolerance | Recommendation |
|----------|------------|----------|----------------|----------------|
| A | <50m² | Any | Any | **Local only** - Import economics don't work |
| B | 50-100m² | <4 months | Low | **Local only** - Timeline too tight for compliance |
| C | 50-100m² | >6 months | Medium-High | **Consider import** - Marginal savings, acceptable risk |
| D | >100m² | >6 months | Any | **Strong import case** - Significant savings, time for due diligence |
| E | >100m² | <4 months | Any | **Hybrid** - Local for this project, establish import relationship for future |

This framework means the reader can self-select their scenario and get a tailored recommendation without me needing to know their exact situation.

---

### Technique 3: The Supplier Vetting Checklist

For any research involving external parties (suppliers, contractors, vendors), create a practical vetting checklist they can use immediately.

**The Prompt:**
```
Based on my research on [evaluating suppliers/contractors/vendors for TOPIC],
create a practical vetting checklist.

Format as a usable document with:

## [Supplier Type] Vetting Checklist

### Phase 1: Desktop Due Diligence (Before Contact)
| Check | How to Verify | Red Flag | Green Flag |
|-------|--------------|----------|------------|

### Phase 2: Initial Engagement (First Contact)
| Question to Ask | Why It Matters | Acceptable Answer | Warning Signs |
|-----------------|----------------|-------------------|---------------|

### Phase 3: Deep Verification (Before Order)
| Verification Step | Method | Cost | Timeline |
|-------------------|--------|------|----------|

### Deal-Breakers (Automatic Disqualification)
- [ ] [Condition 1]
- [ ] [Condition 2]

### Negotiation Leverage Points
- [Point 1]: [How to use it]
```

**Example from my Research:**

Here's part of the actual checklist I created:

**Phase 1: Desktop Due Diligence**
| Check | How to Verify | Red Flag | Green Flag |
|-------|--------------|----------|------------|
| Company registration | Check via China SAIC database | No records, recently registered (<2 years) | 5+ years, consistent registration |
| Export license | Request AQSIQ registration number | Hesitation, "we'll get it" | Immediate documentation |
| Quality certifications | Request certificates, verify issuing body | Unfamiliar certification bodies, expired certs | ISO 9001, CE marking with verifiable numbers |
| Customer references | Ask for SA/Africa references specifically | "Confidential" or only Asian references | Named references willing to speak |

This transforms abstract research into a tool they can use tomorrow.

---

### Technique 4: The Implementation Roadmap

Research is only valuable if it leads to action. End every major report with a time-bound implementation roadmap.

**The Prompt:**
```
Based on this research and recommendation, create an implementation roadmap.

Context:
- Recommended approach: [Your recommendation]
- Key stakeholders: [Who's involved]
- Timeline constraints: [Any deadlines]

Create a roadmap that includes:

## Implementation Roadmap

### Phase 1: [Name] (Week 1-2)
| Action | Owner | Deliverable | Dependencies |
|--------|-------|-------------|--------------|

### Phase 2: [Name] (Week 3-4)
[Same structure]

### Key Milestones
| Milestone | Target Date | Success Criteria |
|-----------|-------------|------------------|

### Risk Checkpoints
| Week | Check | Go/No-Go Criteria |
|------|-------|-------------------|

### Budget Requirements
| Phase | Estimated Cost | Notes |
|-------|----------------|-------|
```

**Example Implementation Roadmap:**

| Week | Action | Owner | Deliverable |
|------|--------|-------|-------------|
| 1 | Submit NRCS Letter of Authority application | Project Manager | Application receipt confirmation |
| 1-2 | Shortlist 3 suppliers from research | PM + Client | Supplier comparison matrix |
| 2 | Request samples from shortlisted suppliers | PM | Sample order confirmations |
| 3-4 | Conduct video factory tours | PM | Tour notes + photos |
| 4-5 | Receive and test samples | PM + Architect | Test results documentation |
| 5 | Final supplier selection | PM + Client | Supplier appointment letter |
| 6 | Negotiate terms and place order | PM | Purchase order + deposit payment |

**Go/No-Go Checkpoints:**
| Week | Decision Point | Criteria to Proceed |
|------|----------------|---------------------|
| 4 | Sample quality | Samples meet SANS 613 requirements |
| 5 | Total landed cost | Savings >15% vs local option |
| 6 | Supplier verification | All due diligence checks passed |

This turns your report from "information" into "action plan."

---

### Technique 5: Appendix Templates That Add Real Value

Most appendices are afterthoughts. These templates make them genuinely useful.

**Appendix A: Compliance Checklist**
```
## SANS/NRCS Compliance Checklist

| Requirement | Standard | Evidence Required | Status | Notes |
|-------------|----------|-------------------|--------|-------|
| [Requirement 1] | SANS [XXX] | [Document type] | [ ] | |
| [Requirement 2] | SANS [XXX] | [Document type] | [ ] | |

### Submission Checklist
- [ ] All certificates attached
- [ ] Test reports included
- [ ] Application form completed
- [ ] Payment proof attached
```

**Appendix B: Cost Calculation Workings**
```
## Landed Cost Calculation: Detailed Workings

### Assumptions
| Assumption | Value | Source | Last Verified |
|------------|-------|--------|---------------|
| Exchange rate | R18.20/USD | XE.com | [Date] |
| Freight rate | $X/container | [Shipping line] | [Date] |

### Calculation Steps
1. FOB Cost: [Calculation]
2. + Freight: [Calculation]
3. = CIF Value: [Result]
4. + Duty ([X]%): [Calculation]
5. + VAT (15%): [Calculation]
6. + Clearing: [Estimate]
7. = Total Landed: [Result]

### Sensitivity: If exchange rate moves to R20/USD
[Recalculation]
```

**Appendix C: Risk Register (Full Version)**
```
## Complete Risk Register

[Full version of risk register with all identified risks, not just top 5]

| ID | Category | Risk | L | I | Score | Mitigation | Owner | Status |
|----|----------|------|---|---|-------|------------|-------|--------|
| R1 | | | | | | | | |
| R2 | | | | | | | | |
[Continue for all risks]

### Risk Review Schedule
- Weekly during [phase]
- Monthly during [phase]
- Review triggers: [Events that prompt immediate review]
```

These appendices demonstrate thoroughness and give readers the raw materials to do their own analysis if they want to dig deeper.

---

## When This Method Works (And When to Hire a Professional)

I've been honest about failures. Let me be equally clear about scope.

### This Method Works Best For:

| Research Type | Why It Works | Example |
|---------------|--------------|---------|
| **Regulatory research** | Rules are documented, AI can synthesize across sources | Import requirements, compliance checklists |
| **Cost modeling** | Structures are standard, AI handles calculations | Landed cost analysis, budget comparisons |
| **Supplier/vendor evaluation** | Criteria are definable, research is systematic | Certification checks, due diligence frameworks |
| **Process documentation** | Steps are logical, AI excels at sequencing | Implementation roadmaps, checklists |
| **Comparison analysis** | Framework is clear, AI handles multiple variables | Option A vs B vs C evaluations |

### Hire a Professional When:

| Situation | Why AI Falls Short | Who to Call |
|-----------|-------------------|-------------|
| **Legal interpretation needed** | AI can't give legal advice, liability matters | Attorney specializing in your domain |
| **Physical verification required** | AI can't inspect products, sites, or people | Inspector, auditor, or on-site representative |
| **Relationship leverage matters** | AI has no network, no favors to call in | Experienced broker, agent, or consultant |
| **Recent regulatory changes** | AI training data is months/years old | Specialist who tracks current requirements |
| **Stakes exceed R500K** | Error cost is too high for unvalidated research | Professional with liability insurance |
| **Domain is unfamiliar to you** | You can't evaluate if AI output is reasonable | Expert who can sanity-check findings |

### The Hybrid Approach (Often Best)

For significant decisions, combine this method with targeted professional input:

1. **Do your AI research first** - 3 hours, free/low cost
2. **Identify specific questions** - What gaps exist? What needs verification?
3. **Book a focused consultation** - 1 hour with an expert, R800-R1,500
4. **Ask targeted questions** - Not "explain everything" but "validate these specific findings"

This hybrid approach costs R1,000-R2,000 instead of R15,000-R25,000, and you get both AI efficiency and professional validation.

---

## Important Limitations (Read This)

This methodology produces **research for decision support**, not professional advice.

**What AI research can do:**
- Synthesize publicly available information
- Structure complex topics into manageable frameworks
- Identify questions you should be asking
- Create checklists and templates for systematic evaluation
- Save significant time on information gathering

**What AI research cannot do:**
- Provide legal, financial, or professional advice
- Access current pricing, exchange rates, or market conditions
- Verify physical reality (product quality, site conditions)
- Replace professional judgment in specialized domains
- Guarantee accuracy—AI confidently produces errors

**Your responsibility:**
- Validate critical findings against primary sources
- Make the "phone call test" for high-stakes decisions
- Recognize when you're outside your competence to evaluate AI output
- Consult professionals when stakes, complexity, or liability warrant it

**Disclaimer:** This methodology is shared for educational purposes. Decisions based on AI-assisted research are your responsibility. For matters involving regulatory compliance, significant financial commitments, or legal obligations, consult qualified professionals.

---

## Bonus: My Actual Prompts File

I keep a `research-prompts.md` file that I copy from for every project. Here's the structure:

```markdown
# Research Prompt Templates

## SCQA Framing
[Template]

## Category Research - Generic
[Template]

## Category Research - Cost Analysis
[Specialized template]

## Category Research - Regulatory/Compliance
[Specialized template]

## Category Research - Supplier/Vendor Evaluation
[Specialized template]

## Category Research - Risk Assessment
[Specialized template]

## Synthesis - Decision Framework
[Template]

## Validation - Quality Check
[Template]

## Report Structure - Executive Summary
[Template]
```

Each template is copy-paste ready. I just fill in the brackets and go.

---

## What's Next

You now have the complete system I use to turn complex questions into decision-ready reports.

**What you can now do:**
- Frame any research question using SCQA (15 minutes)
- Build airtight category structures with MECE (10 minutes)
- Run copy-paste prompts that generate structured output (60-90 minutes)
- Assemble professional reports with proven templates (30 minutes)
- Validate findings with external verification (not just AI checking AI)
- Extract non-obvious insights that elevate your analysis
- Create scenario frameworks that serve multiple stakeholders
- Know when to stop and call a professional

**The realistic economics:**
- Ad-hoc research: 15-20 hours of scattered, unstructured work
- Professional consultation: R15,000-R25,000 for comprehensive analysis
- This method: 3-4 hours (once learned) + optional targeted professional validation (R800-R1,500)
- Hybrid approach: Best of both worlds for R1,500-R3,000 total

**The real transformation:**
You're not just saving money or time. You're building a capability that compounds.

Every report you create with this system makes you faster at the next one. The templates become second nature. The prompts get refined for your specific domain. Your judgment about what matters—and what requires professional validation—gets sharper.

But here's the deeper shift I've noticed: once you internalize this methodology, you start *thinking* differently about complex questions. You automatically frame problems in SCQA. You instinctively look for MECE categories. You catch your own logical gaps before AI even enters the picture.

The Pyramid Principle isn't just about communication—it's about **thinking clearly enough that AI can amplify your clarity**.

That's the unlock that most people miss. They ask AI to think for them. You're using AI to think *with* you—while maintaining the judgment to know its limits.

This isn't just a toolkit. It's a cognitive upgrade.

---

## Your First Project Challenge

Don't let this sit in your "interesting things I read" folder. Apply it this week.

**Pick a decision you've been procrastinating on.** Something with enough complexity that you've been avoiding the research. Run it through SCQA. Build your categories. Use the prompts.

Then reply to this email and tell me:
1. What question did you tackle?
2. What surprised you about the process?
3. Where did you find the AI output needed verification?

I read every response. The best insights in future editions come from readers applying these frameworks to contexts I never imagined.

---

**Need implementation support?** As a paid subscriber, you get direct access. Reply with your SCQA draft and I'll give specific feedback on your framing.

**Hit a wall?** Describe where you're stuck. I've seen most failure patterns and can usually point you in the right direction within a day.

---

<!-- IMAGE: Hero image
PROMPT: A modern desk workspace with a laptop showing a structured document outline, alongside printed templates and checklists. Professional, organized aesthetic. Warm lighting, clean lines. Editorial illustration style suggesting productivity and systematic approach. Muted earth tones with blue accents.
-->

<!-- IMAGE: After Part 2 (MECE section)
PROMPT: A visual diagram showing interconnected boxes arranged in a pyramid structure, with checkmarks indicating validation. Clean, minimal design. Blue and white color scheme. Concept of organized, validated thinking structure.
-->

<!-- IMAGE: After Part 5 (Validation section)
PROMPT: A checklist on a clipboard with some items checked off, next to a coffee cup and pen. Professional, clean aesthetic. Suggesting quality control and thoroughness. Warm tones, editorial illustration style.
-->
