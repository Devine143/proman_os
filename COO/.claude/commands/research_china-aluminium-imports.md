---
allowed-tools: Task, WebSearch, WebFetch, mcp__firecrawl-mcp__firecrawl_scrape, mcp__firecrawl-mcp__firecrawl_search, mcp__perplexity-ask__perplexity_ask, Write, Read
description: Research Chinese aluminium door/window imports to South Africa - suppliers, regulations, costs, logistics
model: sonnet
---

# Research: Aluminium Doors & Windows - China to South Africa Import Analysis

Conduct comprehensive technical and commercial research on importing aluminium doors and windows from China into South Africa to support procurement decision-making for construction projects.

## Research Brief

**Problem Statement:** Evaluate the viability, costs, risks, and regulatory requirements of importing aluminium doors and windows from Chinese manufacturers versus local South African alternatives for construction projects.

**Target Audience:** Construction project managers, quantity surveyors, and procurement specialists requiring detailed technical and commercial analysis.

**Depth Level:** Technical/specialist - detailed specifications, landed cost calculations, compliance requirements, and supplier due diligence.

**Output Format:** Comparative analysis with decision framework and supplier evaluation matrix.

**Constraints:**
- Budget/cost focused: Must include detailed cost breakdowns and ROI analysis
- Time-sensitive: Practical lead times and logistics considerations
- Geographic focus: China (manufacturing) → South Africa (import destination)
- Regulatory compliance: SABS standards, NRCS requirements, import duties, ITAC regulations

## Research Questions

### Primary Questions
1. **Cost Analysis:** What is the true landed cost of Chinese aluminium doors/windows vs. local SA equivalents, including duties, shipping, compliance testing, and hidden costs?

2. **Regulatory Compliance:** What SABS standards, NRCS homologation, and import permits are required? What is the compliance process and timeline?

3. **Supplier Landscape:** Who are the reputable Chinese manufacturers exporting to South Africa, and what is their track record?

### Secondary Questions
4. **Quality Assurance:** How do Chinese products compare to SA products on quality, warranties, and performance specifications (thermal, acoustic, weather resistance)?

5. **Logistics & Lead Times:** What are realistic shipping times, freight costs, and import clearance timelines? What are the risks (port delays, container shortages)?

6. **Trade Considerations:** Are there anti-dumping duties, ITAC investigations, or trade barriers affecting aluminium imports from China?

7. **Local Market Impact:** What are local manufacturers' positions on Chinese imports? Are there Buy Local requirements for certain projects?

8. **Risk Assessment:** What are the key risks (quality inconsistency, communication barriers, warranty enforcement, exchange rate volatility)?

## Research Workflow

### Phase 1: Regulatory Framework Discovery
Use `mcp__perplexity-ask__perplexity_ask` to understand:
- SABS standards for aluminium windows/doors (SANS 613, SANS 10137)
- NRCS compulsory specifications and Letter of Authority requirements
- Import duty rates (HS codes 7610.10, 7610.90, 8302.41)
- ITAC regulations and any anti-dumping measures

### Phase 2: Cost Structure Research
Use `mcp__firecrawl-mcp__firecrawl_search` to find:
- Chinese manufacturer pricing (FOB Guangzhou/Shanghai)
- Shipping costs (FCL rates to Durban/Cape Town)
- Current import duty rates from SARS
- Compliance testing costs in SA
- Freight forwarding and clearing agent fees

### Phase 3: Supplier Intelligence
Use `mcp__firecrawl-mcp__firecrawl_scrape` on:
- Alibaba/Made-in-China top-rated aluminium manufacturers
- Industry publications listing approved exporters
- SA importers' websites for supplier partnerships
- Trade show exhibitor lists (FenestrationChina, Windoor Expo)

### Phase 4: Local Market Comparison
Research South African manufacturers:
- Wispeco, Hulamin, AWS (pricing, lead times, specifications)
- Local fabricators using imported vs. local profiles
- Project case studies comparing imported vs. local

### Phase 5: Deep Extraction on Key Sources
Scrape detailed information from:
- NRCS website (compliance requirements)
- SARS tariff book (duty calculations)
- Shipping line websites (transit times, rates)
- Industry association publications (AAAMSA, SAGGA)

## Data to Capture

### Cost Data
- [ ] FOB price ranges per m² (casement, sliding, fixed)
- [ ] Sea freight rates (20ft/40ft container to CPT/DBN)
- [ ] Import duty percentages
- [ ] VAT calculations
- [ ] NRCS testing/certification costs
- [ ] Clearing and forwarding fees
- [ ] Inland transport costs
- [ ] Currency considerations (USD/ZAR)

### Compliance Data
- [ ] Applicable SANS standards list
- [ ] NRCS LoA application process
- [ ] Testing laboratory options in SA
- [ ] Typical approval timelines
- [ ] Documentation requirements

### Supplier Data
- [ ] Top 10 Chinese manufacturers exporting to Africa
- [ ] Production capacity and certifications
- [ ] Minimum order quantities
- [ ] Payment terms typically offered
- [ ] Quality control processes
- [ ] References/case studies in SA

### Risk Data
- [ ] Quality rejection rates reported
- [ ] Common compliance failures
- [ ] Shipping delay statistics
- [ ] Warranty claim processes
- [ ] Exchange rate impact scenarios

## Report Structure

### 1. Executive Summary
- Key findings in 5 bullet points
- Go/No-Go recommendation with conditions
- Bottom-line cost comparison

### 2. Regulatory Compliance Framework
- Applicable standards (SANS 613, etc.)
- NRCS requirements and process
- Import permits and documentation
- Compliance timeline and costs
- Risk: Non-compliance consequences

### 3. Landed Cost Analysis

| Cost Component | Chinese Import | SA Local | Variance |
|----------------|----------------|----------|----------|
| Product cost/m² | | | |
| Shipping | | | |
| Import duty | | | |
| VAT | | | |
| Compliance testing | | | |
| Clearing/forwarding | | | |
| **Total Landed Cost** | | | |

### 4. Supplier Evaluation Matrix

| Criteria | Weight | Supplier A | Supplier B | Supplier C | SA Local |
|----------|--------|------------|------------|------------|----------|
| Price | 25% | | | | |
| Quality certifications | 20% | | | | |
| Lead time | 15% | | | | |
| MOQ flexibility | 10% | | | | |
| Communication | 10% | | | | |
| References in SA | 10% | | | | |
| Warranty terms | 10% | | | | |
| **Weighted Score** | 100% | | | | |

### 5. Logistics & Timeline Analysis
- Order to delivery timeline (best/worst case)
- Shipping route options
- Port of entry considerations
- Storage and handling requirements

### 6. Risk Assessment Matrix

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Quality non-conformance | | | |
| Compliance rejection | | | |
| Shipping delays | | | |
| Exchange rate movement | | | |
| Communication barriers | | | |
| Warranty enforcement | | | |

### 7. Comparative Analysis Summary
- Scenarios where import makes sense
- Scenarios where local is preferable
- Break-even analysis (order size threshold)
- Project type suitability

### 8. Decision Framework
Flowchart/decision tree for procurement choice based on:
- Project size
- Budget constraints
- Timeline requirements
- Quality specifications
- Client preferences

### 9. Recommendations
- Specific supplier shortlist (if importing)
- Due diligence checklist
- Suggested procurement process
- Contract terms to negotiate

### 10. Appendices
- Detailed HS code classifications
- NRCS application forms reference
- Sample import cost calculation
- Supplier contact details
- Source citations

## Output

Save completed research report to:
`COO/projects/research/china_aluminium_imports_[YYYYMMDD].md`

## Quality Checklist

Before finalizing, verify:
- [ ] All cost figures are current (within 6 months)
- [ ] Regulatory information verified against official sources
- [ ] At least 3 Chinese suppliers researched in detail
- [ ] Local SA benchmark pricing included
- [ ] Risk mitigations are practical and actionable
- [ ] Decision framework is clear and usable
- [ ] All sources cited with dates
