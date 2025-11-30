---
allowed-tools: AskUserQuestion, Write, Edit
description: Create a detailed research prompt through guided questions
argument-hint: [brief topic or area to research]
model: sonnet
---

# Deep Research Prompt Builder

This command guides you through defining a research project, then generates a detailed prompt you can use for deep research. Follow the `Workflow` to gather requirements and produce a tailored research prompt.

## Variables

INITIAL_TOPIC: $1

## Workflow

1. **Gather Research Requirements**

   Use `AskUserQuestion` to ask the following questions (ask all at once):

   **Question 1 - Problem Statement:**
   "What exactly do you want the research to solve or clarify?"
   - Options: Market opportunity analysis, Competitive landscape, Customer/user insights, Strategic decision support, Other

   **Question 2 - Audience & Depth:**
   "Who will read this and how deep should the analysis go?"
   - Options: Executive summary (high-level), Management report (moderate detail), Comprehensive analysis (deep dive), Technical/specialist report

   **Question 3 - Desired Output:**
   "What format should the final deliverable take?"
   - Options: Strategic plan with recommendations, Research report with findings, Comparative analysis, Action-oriented brief

   **Question 4 - Constraints or Focus Areas:**
   "Any specific constraints or areas of focus?"
   - Options: Budget/cost focused, Time-sensitive decisions, Geographic focus (specify), Industry-specific regulations, No specific constraints

2. **Synthesize Requirements**

   Based on the user's answers, identify:
   - The core problem to solve
   - Key research questions to answer
   - Required data types (market data, competitor info, customer insights, etc.)
   - Output structure and depth
   - Any constraints to work within

3. **Generate the Research Prompt**

   Create a detailed prompt using the `Prompt Template` below, customized to the user's requirements.

   Save the prompt to: `COO/.claude/commands/research_[topic-slug].md`

## Prompt Template

```markdown
---
allowed-tools: Task, WebSearch, WebFetch, mcp__firecrawl-mcp__firecrawl_scrape, mcp__firecrawl-mcp__firecrawl_search, mcp__perplexity-ask__perplexity_ask, Write, Read
description: [Generated description based on topic]
model: sonnet
---

# Research: [Topic Title]

Conduct comprehensive research on [TOPIC] to [OUTCOME]. This research should be grounded in data and evidence while surfacing unique perspectives.

## Research Brief

**Problem Statement:** [User's problem statement]
**Target Audience:** [Who will use this]
**Depth Level:** [Summary/Moderate/Comprehensive]
**Output Format:** [Strategic plan/Report/Analysis/Brief]
**Constraints:** [Any limitations or focus areas]

## Research Questions

1. [Primary question derived from problem statement]
2. [Secondary question about market/landscape]
3. [Question about customers/users/stakeholders]
4. [Question about competitors/alternatives]
5. [Question about risks/challenges]

## Research Workflow

1. **Broad Discovery**
   - Use `mcp__firecrawl-mcp__firecrawl_search` to find relevant sources
   - Use `mcp__perplexity-ask__perplexity_ask` for synthesized overviews
   - Identify 10-15 high-value sources

2. **Deep Extraction**
   - Use `mcp__firecrawl-mcp__firecrawl_scrape` on top sources
   - Focus on: [specific data types needed]
   - Capture statistics, quotes, and evidence

3. **Analysis & Synthesis**
   - Cross-reference findings
   - Identify patterns and contradictions
   - Quantify findings where possible

4. **Report Generation**
   - Follow the `Report Structure` below
   - Save to: `COO/projects/research/[topic]_[YYYYMMDD].md`

## Report Structure

[Customized structure based on output format selected - could be:]

### For Strategic Plan:
- Executive Summary
- Situation Analysis
- Strategic Options
- Recommended Approach
- Implementation Roadmap
- Risk Mitigation

### For Research Report:
- Executive Summary
- Background & Context
- Methodology
- Key Findings (with evidence)
- Analysis & Implications
- Recommendations
- Appendix: Sources

### For Comparative Analysis:
- Executive Summary
- Evaluation Criteria
- Option Analysis (matrix format)
- Pros/Cons Summary
- Recommendation
- Decision Framework

### For Action Brief:
- Bottom Line Up Front
- Key Facts
- Options
- Recommendation
- Next Steps
```

## Report

After generating the prompt:

1. **Confirm** the saved location of the new research prompt
2. **Summarize** the research scope that was defined
3. **Explain** how to use the generated prompt
4. **Offer** to run the research immediately or let the user review the prompt first
