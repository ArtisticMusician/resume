import argparse
import os
from datetime import datetime
from markdown_pdf import MarkdownPdf, Section

def create_pdf(markdown_file, css_file, output_file):
    """
    Converts a Markdown file to a styled PDF using an external CSS file.
    """
    # --- Input File Validation ---
    if not os.path.exists(markdown_file):
        print(f"Error: Markdown file not found at '{markdown_file}'")
        return
    if not os.path.exists(css_file):
        print(f"Error: CSS file not found at '{css_file}'")
        return

    print(f"-> Reading Markdown from: {markdown_file}")
    print(f"-> Reading styles from:   {css_file}")

    # --- Read content from external files ---
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read() # <-- FIX: Read markdown content into a variable

    with open(css_file, 'r', encoding='utf-8') as f:
        stylesheet = f.read()

    # --- Conversion Process ---
    pdf = MarkdownPdf(
        toc_level=0  # Set to 0 to disable table of contents
    )
    
    # <-- FIX: Pass the markdown_content variable directly into the Section
    pdf.add_section(
        Section(markdown_content, toc=False),
        user_css=stylesheet
    )
    
    print(f"-> Saving PDF to:         {output_file}")
    pdf.save(output_file)

    print("\n✅ Conversion successful!")


def main():
    """
    Parses command-line arguments and runs the PDF conversion.
    """
    # Generate the default output filename based on the current date
    date_str = datetime.now().strftime("%Y%m%d")
    default_output = f"{date_str}_resume.pdf"

    parser = argparse.ArgumentParser(
        description="Convert a Markdown file to a styled PDF."
    )

    parser.add_argument(
        "-m", "--markdown",
        default="resume.md",
        help="Input Markdown file (default: resume.md)"
    )
    parser.add_argument(
        "-c", "--css",
        default="styles.css",
        help="CSS stylesheet file (default: styles.css)"
    )
    parser.add_argument(
        "-o", "--output",
        default=default_output,
        help=f"Output PDF file (default: {default_output})"
    )

    args = parser.parse_args()

    create_pdf(args.markdown, args.css, args.output)


if __name__ == "__main__":
    main()