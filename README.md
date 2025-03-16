# Document Comparison

A Python tool for comparing documents (PDF, DOCX) to detect and summarize differences at the word level.

## Features
- Compare **PDF** and **DOCX** files.
- Word-by-word comparison highlighting **added** and **removed** words.
- Outputs a detailed summary of changes including word positions.

## Libraries
- `pdfminer.six` for PDF text extraction.
- `python-docx` for DOCX file handling.
- `difflib` for text comparison.

## Installation
1. Clone the repository.
2. Set up a Python virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Extract text from two documents (PDF or DOCX).
2. Compare documents using the `compare_documents` function.
3. View the changes in the generated summary.

## Example Output:
```plaintext
Removed: 'Certificate' at position 0
Added: 'Md.' at position 1
Added: 'Sajjadur' at position 2
Added: 'Rahman' at position 3
Added: 'Date' at position 4
```
