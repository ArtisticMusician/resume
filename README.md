# Markdown to PDF Resume Converter (Conda Edition)

A simple and powerful Python script for converting a Markdown resume into a beautifully styled, professional PDF.

This guide provides setup and usage instructions for users managing their environments with Conda.

## Features

- **Clean Conversion:** Converts standard Markdown to a high-quality PDF.
- **Fully Stylable:** Uses an external CSS file (`styles.css`) for complete control over the PDF's appearance.
- **Dynamic Filename:** Automatically names the output file with the current date (e.g., `20251108_resume.pdf`).
- **Command-Line Interface:** Flexible arguments allow you to specify custom input and output files.
- **Page Break Control:** Add page breaks directly in your Markdown for perfect layout control.

## Requirements

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution) installed.

## Installation and Setup (Conda Workflow)

Follow these steps in your terminal to set up a dedicated Conda environment for this project.

### 1. Create the Conda Environment

First, create a new, clean environment for the project. We'll name it `resume_conda` and install Python in it.

 conda create --name resume_conda python=3.10

*(The command will ask you to proceed (`y/n`). Type `y` and press Enter.)*

### 2. Activate the Environment

Before you can use the environment or install packages, you must activate it.

 conda activate resume_conda

Your terminal prompt should now change to show `(resume_conda)` at the beginning, indicating that the environment is active.

### 3. Install Dependencies

With the environment active, install the necessary Python library using `pip`. Pip works perfectly inside a Conda environment for packages that aren't on Conda channels.

 pip install markdown-pdf

The setup is now complete! You only need to do these steps once.

---

## How to Use

Make sure your `resume_conda` environment is active before running the script. If it's not, run `conda activate resume_conda`.

### 1. Basic Usage (Default Files)

This is the simplest way to use the script. It assumes your files are named `resume.md` and `styles.css`.

1. Edit `resume.md` with your personal information.
2. (Optional) Modify `styles.css` to change the look and feel.
3. Run the script from your terminal:
  
  python convert.py

This will create a new PDF in the same directory named `YYYYMMDD_resume.pdf`.

### 2. Advanced Usage (Custom Files)

Use command-line arguments to specify your own input and output files.

- `-m` or `--markdown`: Specify the input Markdown file.
- `-c` or `--css`: Specify the CSS stylesheet.
- `-o` or `--output`: Specify the name for the output PDF.

**Example:**

 python convert.py --markdown dev_resume.md --css blue_theme.css --output dev_resume_final.pdf

### 3. Deactivating the Environment

When you are finished using the script, you can deactivate the environment to return to your base terminal session.

 conda deactivate

---

## Customization

### Editing Content

Modify the `resume.md` file. The script will use whatever content is saved in that file.

### Editing Style

Modify the `styles.css` file to change fonts, colors, margins, spacing, and more.

### Adding Page Breaks

To force a page break in your document, insert the following HTML snippet on a new line in your `resume.md` file:

 <div class="page-break"></div>

The styles for this are already included in the `styles.css` file.

## File Structure

- `convert.py`: The core Python script that performs the conversion.
- `resume.md`: Your resume content, written in Markdown.
- `styles.css`: The stylesheet that defines the visual appearance of the final PDF.
- `README.md`: These instructions.