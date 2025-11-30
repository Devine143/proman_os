---
description: Analyze large PDF documents with automatic processing and splitting
tags: [project]
---

You are helping analyze a large PDF document that may exceed standard size limits.

**Prerequisites:**
- Python virtual environment must exist at `/Users/donovan/AGENT/.venv`
- PyPDF2 must be installed: `uv pip install PyPDF2`
- If venv doesn't exist, create it: `uv venv && source .venv/bin/activate && uv pip install PyPDF2`

**Your Task:**
1. **Always extract PDF to markdown first** (regardless of file size, because file size ≠ text content size)
   - Use: `.venv/bin/python /Users/donovan/AGENT/scripts/process_large_pdf.py "[file]" --extract-text`
   - This creates a markdown version in a `processed/` subdirectory
   - The markdown file will be named: `[original_filename]_text.md`

2. **Check the extracted markdown file size:**
   - If markdown is manageable (< 100 pages): Launch doc-analyzer on the full markdown
   - If markdown is very large (> 100 pages): Split the analysis into sections or use context-aware chunking

3. **Launch doc-analyzer agent:**
   - Provide the path to the extracted markdown file (not the original PDF)
   - Provide the path to the original PDF for reference metadata
   - Doc-analyzer will create a summary alongside the markdown file

4. **If analysis fails due to size:**
   - Use the split option: `.venv/bin/python /Users/donovan/AGENT/scripts/process_large_pdf.py "[file]" --split 50 --extract-text`
   - This creates 50-page PDF chunks AND markdown extracts
   - Launch doc-analyzer on each markdown chunk in parallel
   - Combine insights from all analyses into comprehensive summary
5. **Deliver PM-critical information:**
   - Key decisions needed
   - Timeline impacts
   - Budget implications
   - Risk factors
   - Action items for Donovan
   - Stakeholder communication needs

**Processing Strategy:**
- **ALL PDFs:** Extract to markdown first (file size is misleading - a 600KB PDF can be 200+ pages of text)
- **< 100 pages:** Analyze full markdown with doc-analyzer
- **100-300 pages:** Analyze full markdown (may need multiple passes)
- **> 300 pages:** Split into 50-page chunks, analyze each, combine results

**Output Format:**
Present results in this structure:
```markdown
# Document Analysis: [Document Name]

## Executive Summary
[2-3 sentence overview of document purpose and PM impact]

## Critical Decisions Required
- [Decision 1 with deadline]
- [Decision 2 with deadline]

## Timeline Impact
[Any schedule implications]

## Budget Impact
[Any cost implications]

## Risk Factors
[Key risks identified]

## Action Items for PM
1. [Action with owner and deadline]
2. [Action with owner and deadline]

## Stakeholder Communication
[Who needs to be informed about what]

## Technical Details
[Relevant specs, requirements, compliance items]
```

**Special Instructions:**
- Always prioritize PM-actionable information over technical details
- Flag anything requiring immediate attention
- Identify missing information that needs follow-up
- Cross-reference with PMP framework knowledge areas when relevant
- Use Proman's core values (H.R.I.G.I.) when making recommendations
