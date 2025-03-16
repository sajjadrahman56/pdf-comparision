import pdfminer.high_level
import difflib
import docx

def extract_text_from_pdf(pdf_file):
    return pdfminer.high_level.extract_text(pdf_file)

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    return "\n".join([para.text for para in doc.paragraphs])

def compare_words(word_list1, word_list2):
    diff = difflib.ndiff(word_list1, word_list2)
    changes = []

    for i, change in enumerate(diff):
        if change.startswith("+ "):
            changes.append(f"Added: '{change[2:]}' at position {i}")
        elif change.startswith("- "):
            changes.append(f"Removed: '{change[2:]}' at position {i}")
    
    return "\n".join(changes)

def compare_documents(file1, file2):
    if file1.endswith(".pdf") and file2.endswith(".pdf"):
        text1 = extract_text_from_pdf(file1)
        text2 = extract_text_from_pdf(file2)
    elif file1.endswith(".docx") and file2.endswith(".docx"):
        text1 = extract_text_from_docx(file1)
        text2 = extract_text_from_docx(file2)
    else:
        return "Unsupported file formats."
    
    # Split the text into words for finer comparison
    words1 = text1.split()
    words2 = text2.split()

    # Compare word by word
    changes = compare_words(words1, words2)
    return changes if changes else "No significant differences."

# Example usage
file1 = "1_p.pdf"
file2 = "3_p.pdf"
result = compare_documents(file1, file2)
print("Summary of Changes:\n", result)
