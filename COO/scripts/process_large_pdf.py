#!/usr/bin/env python3
"""
Process Large PDF Documents for Analysis
Handles compression, splitting, and text extraction for PM documents

Usage with UV:
    uv run /Users/donovan/AGENT/scripts/process_large_pdf.py document.pdf --compress --split 50
"""

import os
import sys
import argparse
from pathlib import Path

def check_dependencies():
    """Check if required tools are installed"""
    try:
        import PyPDF2
        return True
    except ImportError:
        print("❌ PyPDF2 not installed. Installing with uv...")
        os.system("uv pip install PyPDF2")
        import PyPDF2
        return True

def get_pdf_info(pdf_path):
    """Get PDF file information"""
    import PyPDF2

    file_size = os.path.getsize(pdf_path) / (1024 * 1024)  # MB

    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        num_pages = len(reader.pages)

        # Try to get document info
        metadata = reader.metadata
        title = metadata.get('/Title', 'Unknown') if metadata else 'Unknown'

    return {
        'size_mb': file_size,
        'num_pages': num_pages,
        'title': title
    }

def compress_pdf(input_path, output_path):
    """Compress PDF using Ghostscript"""
    print(f"\n📦 Compressing PDF...")

    cmd = f"""gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite \
        -dCompatibilityLevel=1.4 \
        -dPDFSETTINGS=/ebook \
        -sOutputFile="{output_path}" \
        "{input_path}" 2>/dev/null"""

    result = os.system(cmd)

    if result == 0 and os.path.exists(output_path):
        original_size = os.path.getsize(input_path) / (1024 * 1024)
        compressed_size = os.path.getsize(output_path) / (1024 * 1024)
        reduction = ((original_size - compressed_size) / original_size) * 100

        print(f"✅ Compressed: {original_size:.1f}MB → {compressed_size:.1f}MB ({reduction:.0f}% reduction)")
        return output_path
    else:
        print(f"⚠️ Compression failed or Ghostscript not installed")
        return input_path

def split_pdf(input_path, output_dir, pages_per_chunk=50):
    """Split PDF into chunks"""
    import PyPDF2

    print(f"\n✂️ Splitting PDF into {pages_per_chunk}-page chunks...")

    with open(input_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        total_pages = len(reader.pages)

        chunk_num = 1
        output_files = []

        for start_page in range(0, total_pages, pages_per_chunk):
            end_page = min(start_page + pages_per_chunk, total_pages)

            writer = PyPDF2.PdfWriter()
            for page_num in range(start_page, end_page):
                writer.add_page(reader.pages[page_num])

            output_path = os.path.join(output_dir, f'chunk_{chunk_num}_pages_{start_page+1}-{end_page}.pdf')
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

            print(f"  ✅ Chunk {chunk_num}: Pages {start_page+1}-{end_page} → {output_path}")
            output_files.append(output_path)
            chunk_num += 1

    return output_files

def extract_text(input_path, output_path):
    """Extract text from PDF to markdown"""
    import PyPDF2

    print(f"\n📄 Extracting text to markdown...")

    with open(input_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)

        markdown_content = f"# Document: {Path(input_path).stem}\n\n"
        markdown_content += f"**Total Pages:** {len(reader.pages)}\n\n"
        markdown_content += "---\n\n"

        for page_num, page in enumerate(reader.pages, 1):
            text = page.extract_text()
            markdown_content += f"## Page {page_num}\n\n"
            markdown_content += text + "\n\n"
            markdown_content += "---\n\n"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"✅ Text extracted to: {output_path}")
    return output_path

def main():
    parser = argparse.ArgumentParser(description='Process large PDF documents for analysis')
    parser.add_argument('input_pdf', help='Path to input PDF file')
    parser.add_argument('--compress', action='store_true', help='Compress PDF first')
    parser.add_argument('--split', type=int, metavar='PAGES', help='Split into chunks of N pages')
    parser.add_argument('--extract-text', action='store_true', help='Extract text to markdown')
    parser.add_argument('--output-dir', help='Output directory (default: same as input)')

    args = parser.parse_args()

    # Check dependencies
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

    current_file = args.input_pdf

    # Compress if requested
    if args.compress:
        compressed_path = os.path.join(output_dir, f"{Path(args.input_pdf).stem}_compressed.pdf")
        current_file = compress_pdf(args.input_pdf, compressed_path)

    # Split if requested
    if args.split:
        split_files = split_pdf(current_file, output_dir, args.split)
        print(f"\n✅ Created {len(split_files)} chunks in: {output_dir}")

    # Extract text if requested
    if args.extract_text:
        text_path = os.path.join(output_dir, f"{Path(args.input_pdf).stem}_text.md")
        extract_text(current_file, text_path)

    print(f"\n✅ Processing complete!")
    print(f"📁 Output directory: {output_dir}")

    # Provide usage suggestions
    if args.split:
        print(f"\n💡 Next steps:")
        print(f"   1. Review chunks in: {output_dir}")
        print(f"   2. Use doc-analyzer agent on each chunk")
        print(f"   3. Combine insights from all chunks")

if __name__ == '__main__':
    main()
