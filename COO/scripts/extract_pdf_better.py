#!/usr/bin/env python3
"""
Better PDF Extraction for Analysis
Uses pymupdf4llm for high-quality markdown conversion with preserved formatting

Usage:
    .venv/bin/python /Users/donovan/AGENT/scripts/extract_pdf_better.py document.pdf
    .venv/bin/python /Users/donovan/AGENT/scripts/extract_pdf_better.py document.pdf --pages 50
"""

import os
import sys
import argparse
from pathlib import Path

def check_dependencies():
    """Check and install required libraries"""
    required = {
        'pymupdf4llm': 'pymupdf4llm',
        'PyMuPDF': 'pymupdf'
    }

    for module, package in required.items():
        try:
            __import__(module)
        except ImportError:
            print(f"📦 Installing {package}...")
            os.system(f"uv pip install {package}")

def get_pdf_info(pdf_path):
    """Get PDF metadata"""
    import fitz  # PyMuPDF

    file_size = os.path.getsize(pdf_path) / (1024 * 1024)  # MB

    doc = fitz.open(pdf_path)
    num_pages = len(doc)
    metadata = doc.metadata

    doc.close()

    return {
        'size_mb': file_size,
        'num_pages': num_pages,
        'title': metadata.get('title', 'Unknown'),
        'author': metadata.get('author', 'Unknown')
    }

def extract_to_markdown(pdf_path, output_path, pages_per_chunk=None):
    """
    Extract PDF to markdown using pymupdf4llm
    Preserves formatting, tables, and structure
    """
    import pymupdf4llm

    print(f"\n📄 Extracting PDF to markdown with pymupdf4llm...")
    print(f"   This preserves formatting, tables, and document structure")

    if pages_per_chunk:
        print(f"   Processing in chunks of {pages_per_chunk} pages...")

        # Get total pages
        import fitz
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        doc.close()

        # Process in chunks
        all_markdown = []
        chunk_num = 1

        for start_page in range(0, total_pages, pages_per_chunk):
            end_page = min(start_page + pages_per_chunk, total_pages)

            print(f"   Processing pages {start_page + 1}-{end_page}...")

            # Extract this chunk
            md_text = pymupdf4llm.to_markdown(
                pdf_path,
                pages=list(range(start_page, end_page))
            )

            all_markdown.append(f"\n\n---\n# CHUNK {chunk_num}: Pages {start_page + 1}-{end_page}\n---\n\n")
            all_markdown.append(md_text)
            chunk_num += 1

        final_markdown = "".join(all_markdown)
    else:
        # Extract entire document at once
        print(f"   Processing entire document...")
        final_markdown = pymupdf4llm.to_markdown(pdf_path)

    # Save to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_markdown)

    file_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
    print(f"✅ Markdown saved: {output_path}")
    print(f"   Size: {file_size:.1f} MB")

    return output_path

def split_pdf(pdf_path, output_dir, pages_per_chunk):
    """Split PDF into smaller PDF files"""
    import fitz

    print(f"\n✂️ Splitting PDF into {pages_per_chunk}-page chunks...")

    doc = fitz.open(pdf_path)
    total_pages = len(doc)

    chunk_files = []
    chunk_num = 1

    for start_page in range(0, total_pages, pages_per_chunk):
        end_page = min(start_page + pages_per_chunk, total_pages)

        # Create new PDF with this chunk
        chunk_doc = fitz.open()
        chunk_doc.insert_pdf(doc, from_page=start_page, to_page=end_page - 1)

        chunk_path = os.path.join(output_dir, f'chunk_{chunk_num}_pages_{start_page+1}-{end_page}.pdf')
        chunk_doc.save(chunk_path)
        chunk_doc.close()

        print(f"  ✅ Chunk {chunk_num}: Pages {start_page+1}-{end_page} → {chunk_path}")
        chunk_files.append(chunk_path)
        chunk_num += 1

    doc.close()
    return chunk_files

def main():
    parser = argparse.ArgumentParser(
        description='Extract PDF to high-quality markdown using pymupdf4llm'
    )
    parser.add_argument('input_pdf', help='Path to input PDF file')
    parser.add_argument('--pages', type=int, metavar='N',
                       help='Process in chunks of N pages (useful for very large PDFs)')
    parser.add_argument('--split', action='store_true',
                       help='Also split PDF into separate files')
    parser.add_argument('--output-dir', help='Output directory (default: same as input)')

    args = parser.parse_args()

    # Check dependencies
    print("🔍 Checking dependencies...")
    check_dependencies()

    # Validate input
    if not os.path.exists(args.input_pdf):
        print(f"❌ File not found: {args.input_pdf}")
        sys.exit(1)

    # Setup output directory
    if args.output_dir:
        output_dir = args.output_dir
    else:
        output_dir = os.path.join(os.path.dirname(args.input_pdf), 'processed')

    os.makedirs(output_dir, exist_ok=True)

    # Get PDF info
    print(f"\n📊 Analyzing PDF...")
    info = get_pdf_info(args.input_pdf)
    print(f"  Size: {info['size_mb']:.1f} MB")
    print(f"  Pages: {info['num_pages']}")
    print(f"  Title: {info['title']}")
    print(f"  Author: {info['author']}")

    # Extract to markdown
    output_path = os.path.join(output_dir, f"{Path(args.input_pdf).stem}_enhanced.md")
    extract_to_markdown(args.input_pdf, output_path, pages_per_chunk=args.pages)

    # Split PDF if requested
    if args.split:
        pages_per_chunk = args.pages or 50
        split_pdf(args.input_pdf, output_dir, pages_per_chunk)

    print(f"\n✅ Processing complete!")
    print(f"📁 Output directory: {output_dir}")
    print(f"\n💡 Next steps:")
    print(f"   1. Review markdown: {output_path}")
    print(f"   2. Use doc-analyzer agent on the markdown file")
    print(f"   3. Quality should be significantly better than basic PyPDF2 extraction")

if __name__ == '__main__':
    main()
