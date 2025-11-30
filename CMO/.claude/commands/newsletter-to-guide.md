---
description: Transform a completed newsletter into a comprehensive PDF-ready guide with research enrichment
argument-hint: path/to/newsletter.md
model: sonnet
allowed-tools: mcp__perplexity-ask__perplexity_ask, Read, Write, Glob, AskUserQuestion
---

# Newsletter to Guide Transformation

Transform the newsletter at `$ARGUMENTS` into a comprehensive PDF-ready guide using the guide-creation-methodology.md as the master reference.

---

## Phase 1: Newsletter Analysis

First, read the newsletter file and the guide methodology:

1. **Read the newsletter** at the provided path
2. **Read the methodology** at `/Users/donovan/PROMAN_OS/CMO/guide-creation-methodology.md`

Then analyze the newsletter to identify:

### Archetype Detection (Use Decision Tree)

```
START HERE
    │
    ▼
Is this about BUILDING something (system/workflow/tool)?
    │
    ├── YES → Is it technical with code/config?
    │           ├── YES → IMPLEMENTATION BLUEPRINT
    │           └── NO  → SYSTEM BUILDER
    │
    └── NO ↓

Is this about a PROFESSIONAL METHODOLOGY?
    │
    ├── YES → CONSULTING FRAMEWORK
    │
    └── NO ↓

Is this about PERSONAL TRANSFORMATION or clarity?
    │
    ├── YES → SELF-DISCOVERY GUIDE
    │
    └── NO ↓

Is this about STARTING/GROWING a business?
    │
    ├── YES → BUSINESS BUILDER
    │
    └── NO ↓

Is this about RESEARCH or analysis?
    │
    └── YES → RESEARCH ACCELERATOR
```

### Extract From Newsletter:
- **Title and topic** - The core subject matter
- **Transformation** - The before → after states (what problem → what outcome)
- **Existing framework** - Any numbered steps, phases, or methodology already present
- **Key prompts** - Any AI prompts included
- **Unique insights** - The distinctive perspective or approach

---

## Phase 2: Display Analysis

Present your analysis in this format:

```
═══════════════════════════════════════════════════════════════
                    NEWSLETTER ANALYSIS
═══════════════════════════════════════════════════════════════

**Source:** [filename]
**Detected Archetype:** [archetype name]
**Confidence:** [high/medium/low]

**Archetype Signals Found:**
• [signal 1 from methodology that matched]
• [signal 2]
• [signal 3]

───────────────────────────────────────────────────────────────

**Transformation Identified:**
• Before: [current state of reader]
• After: [transformed state after applying guide]

**Existing Framework:**
[X]-step [framework name/description]
• Step 1: [name]
• Step 2: [name]
• [etc.]

───────────────────────────────────────────────────────────────

**Title Options:**
1. [Title] — [The Complete Guide]
2. [Title] — [A Practical Framework]
3. [Title] — [From X to Y]

═══════════════════════════════════════════════════════════════
```

---

## Phase 3: Perplexity Research

Execute 3-5 research queries using mcp__perplexity-ask__perplexity_ask to enrich the guide:

### Query 1: Best Practices
```
Research current best practices for [TOPIC] in 2024-2025. Focus on:
- Expert-recommended approaches
- Industry standards
- Proven methodologies
- Recent developments or shifts in thinking
```

### Query 2: Common Pitfalls
```
What are the most common mistakes and pitfalls experts identify when [TOPIC ACTIVITY]? Include:
- Root causes of failures
- Warning signs to watch for
- How experienced practitioners avoid these issues
```

### Query 3: Monetization/Business Opportunities
```
What are the business and monetization opportunities around [TOPIC]? Include:
- Service packaging options
- Market demand indicators
- Pricing benchmarks
- Revenue potential
```

### Query 4: Statistics and Data
```
What statistics, data, and market research support the importance of [TOPIC]? Include:
- Market size and growth
- Adoption rates
- ROI data
- Industry benchmarks
```

### Query 5: Complementary Frameworks
```
What established frameworks or methodologies complement [TOPIC]? Include:
- Related approaches that integrate well
- Foundational theories to reference
- Expert names and credentials to cite
```

---

## Phase 4: Display Research & Defaults

Present research findings and proposed section plan:

```
═══════════════════════════════════════════════════════════════
                    RESEARCH INSIGHTS
═══════════════════════════════════════════════════════════════

**Best Practices Found:**
• [Key best practice 1 with source]
• [Key best practice 2 with source]
• [Key best practice 3 with source]

**Recent Developments:**
• [Relevant news/updates that strengthen the guide]

**Complementary Frameworks:**
• [Related methodology that could be integrated]

**Statistics/Data:**
• [Relevant stats to include for credibility]

**Common Pitfalls:**
• [Expert-identified mistakes to address in Risk section]

───────────────────────────────────────────────────────────────

**Section Plan:**
1. Hook: [Proposed hook approach based on archetype template]
2. Context: [Why this matters now + industry data from research]
3. Core Framework: [X-step system expanded + best practices integration]
4. Monetization: [Service packaging + market opportunity data]
5. Risk Mitigation: [Common pitfalls from research + expert warnings]
6. Action Plan: [Implementation roadmap]
7. Appendix: [Prompt library, templates, resources, further reading]

═══════════════════════════════════════════════════════════════

Proceed with these defaults? [Y/n/edit]
```

---

## Phase 5: User Override (Optional)

Use AskUserQuestion if user wants changes:

**Question options:**
- Different archetype selection
- Modified transformation framing
- Alternative title choice
- Section adjustments
- Additional research focus areas

After gathering any overrides, incorporate them into the plan.

---

## Phase 6: Full Guide Generation

Generate the complete guide using:

1. **guide-creation-methodology.md** as master reference for:
   - 7-section architecture (pages 36-91 of methodology)
   - Selected archetype template
   - Prompt library patterns
   - Quality standards

2. **Newsletter content** as source material for:
   - Core framework to expand
   - Existing prompts to include
   - Author's voice and perspective
   - Personal examples and stories

3. **Perplexity research** for:
   - Best practices integration
   - Statistics and credibility data
   - Risk mitigation content
   - Monetization guidance
   - Citations and sources

### Section-by-Section Generation:

**Section 1: The Hook (1-2 pages)**
Use Template A from methodology:
- Value proposition
- "You'll learn how to:" bullets
- Transformation statement
- Table of Contents
- Quickstart section

**Section 2: The Context (2-3 pages)**
Use Template B from methodology:
- Why This Matters Now (with research data)
- The New Reality (value anchoring)
- The AI Advantage block
- Who This Is For

**Section 3: Core Framework (8-12 pages)**
Use Template C from methodology:
- Expand newsletter's existing framework
- Add Strategic Rationale to each step
- Include prompts with [PLACEHOLDERS]
- Add Pro Tips (from research best practices)
- Add Common Mistakes (from research pitfalls)
- Add "Why This Works" explanations
- Include checkpoints between steps

**Section 4: Monetization & Scaling (3-4 pages)**
Use Template D from methodology:
- 3-tier service packaging with prices
- Revenue projections (from research data)
- Value anchoring against alternatives
- ROI calculations

**Section 5: Risk Mitigation (2-3 pages)**
Use Template E from methodology:
- 5-7 pitfalls with solutions (from research)
- Critical Success Factors (3 non-negotiables)
- Risk Mitigation Matrix

**Section 6: Action Plan (2-3 pages)**
Use Template F from methodology:
- 4-phase implementation roadmap
- Key metrics to track
- "Your Next 3 Steps"
- Resources and further reading

**Section 7: Appendix (2-4 pages)**
- Complete prompt library (all prompts in one place)
- Cheat sheet / quick reference
- Tool links and resources
- Sources from Perplexity research

---

## Phase 7: Output

Save the completed guide to:

```
/Users/donovan/PROMAN_OS/CMO/newsletter-drafts/guides/[slug]-guide.md
```

Where `[slug]` is derived from the newsletter title (lowercase, hyphenated).

### Final Output Format:

```markdown
# [GUIDE TITLE]

*[Subtitle: The transformation promise]*

---

## Table of Contents

1. [Section 1 Name]
2. [Section 2 Name]
... etc.

---

## Quickstart

[For impatient readers - immediate value]

---

## Section 1: [Hook/Introduction]

[Content...]

---

[Continue with all sections...]

---

## Appendix

### Complete Prompt Library

[All prompts organized by category]

### Resources

[Tools, links, further reading]

### Sources

[Citations from Perplexity research]

---

*Generated from: [original newsletter filename]*
*Guide version: 1.0*
*Created: [date]*
```

---

## Quality Checklist (Before Saving)

Verify the guide meets minimum standards from methodology:

- [ ] Transformation is crystal clear (before → after)
- [ ] Value in first 5 pages (quickstart + hook)
- [ ] All prompts are copy-paste ready with [PLACEHOLDERS]
- [ ] Professional structure (McKinsey-style)
- [ ] Specific numbers/metrics included
- [ ] Creates desire for newsletter subscription
- [ ] Sources cited in appendix

---

## Success Criteria

The command succeeds when:
1. Newsletter is analyzed and archetype detected
2. 3-5 Perplexity research queries executed
3. User has opportunity to override defaults
4. Complete 7-section guide generated
5. Guide saved to newsletter-drafts/guides/
6. Quality checklist items satisfied
