import fitz  # PyMuPDF
import re
import os

# from app.services.information_extractor import extract_candidate_information
from app.services.information_extractor import (extract_candidate_information)


def clean_text(text):
    """
    Clean extracted resume text while preserving structure.
    """

    # Normalize line breaks
    text = re.sub(r'\r\n', '\n', text)

    # Remove excessive blank lines
    text = re.sub(r'\n{2,}', '\n\n', text)

    # Remove excessive spaces/tabs
    text = re.sub(r'[ \t]+', ' ', text)

    return text.strip()


def extract_resume_text(pdf_path):
    """
    Extract text from a PDF resume.
    """

    try:
        doc = fitz.open(pdf_path)

        full_text = ""

        for page in doc:
            text = page.get_text()
            full_text += text

        cleaned_text = clean_text(full_text)

        result = {
            "filename": os.path.basename(pdf_path),
            "num_pages": len(doc),
            "text": cleaned_text
        }

        return result

    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return None


if __name__ == "__main__":

    sample_resume = "data/resumes/moderate_candidate_resume.pdf"

    result = extract_resume_text(sample_resume)

    if result:

        print("\n===== RESUME PARSED SUCCESSFULLY =====\n")

        print(f"Filename: {result['filename']}")
        print(f"Pages: {result['num_pages']}\n")

        print("===== EXTRACTED TEXT PREVIEW =====\n")

        print(result["text"][:2000])  # Preview first 2000 chars

        # Extract structured candidate information
        candidate_info = extract_candidate_information(result["text"])

        print("\n===== EXTRACTED CANDIDATE INFORMATION =====\n")

        for key, value in candidate_info.items():
            print(f"{key}: {value}")