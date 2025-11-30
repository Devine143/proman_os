# COO Scripts

Utility scripts for the COO system.

---

## Active Scripts

### extract_pdf_better.py

**Purpose:** Enhanced PDF text extraction with improved formatting and structure preservation

**Function:**
- Extracts text from PDF files using PyMuPDF
- Preserves document structure and formatting
- Handles complex layouts and multi-column documents
- Outputs clean, readable markdown text

**Usage:**
```bash
python ~/AGENT/scripts/extract_pdf_better.py <pdf_file>
```

**Integration:**
- Used by `/analyze_large_doc` slash command
- Called by `process_large_pdf.py` for large documents
- Supports doc-analyzer subagent workflows

---

### process_large_pdf.py

**Purpose:** Process large PDF documents by splitting and compressing for analysis

**Function:**
- Checks PDF file size and complexity
- Compresses large PDFs to reduce file size
- Splits oversized PDFs into manageable chunks
- Prepares documents for AI analysis

**Usage:**
```bash
python ~/AGENT/scripts/process_large_pdf.py <pdf_file>
```

**Output:**
- Compressed PDF (if size > threshold)
- Split PDF chunks (if necessary)
- Processing metadata and logs

**Integration:**
- Automatically called by `/analyze_large_doc` command
- Enables doc-analyzer to handle documents > 15MB
- Supports large spec sheets, reports, and contracts

---

### combine_budget_excel_files.py

**Purpose:** Combine multiple budget analysis Excel files into a single workbook

**Function:**
- Combines 4 budget Excel files into one workbook with separate sheets
- Preserves all formulas, formatting, and cell styling
- Maintains column widths, row heights, and merged cells
- Creates client-ready consolidated workbook

**Usage:**
```bash
python3 ~/AGENT/scripts/combine_budget_excel_files.py <project_name> <date_YYYYMMDD> <output_dir>
```

**Example:**
```bash
python3 ~/AGENT/scripts/combine_budget_excel_files.py "11_Buck_Road" "20251119" "/path/to/output"
```

**Input Files (must exist in output_dir):**
- `{project}_EVM_{date}.xlsx`
- `{project}_Variance_Analysis_{date}.xlsx`
- `{project}_Corrective_Actions_{date}.xlsx`
- `{project}_Cash_Flow_{date}.xlsx`

**Output:**
- `{project}_Budget_Analysis_Complete_{date}.xlsx` with 4 sheets:
  - EVM Metrics
  - Variance Analysis
  - Corrective Actions
  - Cash Flow Forecast

**Integration:**
- Used by `budget-template-filler` subagent (Step 6)
- Part of automated budget status reporting workflow
- Called after individual Excel templates are filled

**Related Documentation:**
- [SOP: Budget Status Reporting](../sops/sop-budget-status-reporting.md)

---

## Directory Structure

```
COO/scripts/
├── extract_pdf_better.py          # Enhanced PDF text extraction
├── process_large_pdf.py           # Large PDF processing & splitting
└── combine_budget_excel_files.py  # Combine budget Excel templates
```

---

## Technical Details

### Requirements

- Python 3.7+
- PyMuPDF (for PDF scripts)
- openpyxl (for Excel scripts)

---

## Design Philosophy

**Prefer:**
- Configuration over code
- AI agents over scripts
- Declarative workflows over imperative programs
- Reusable patterns over one-off solutions

**Use scripts when:**
- External system integration required
- Performance-critical operations needed
- Batch processing required
- System utilities needed

---

**Last Updated:** 2025-11-29
