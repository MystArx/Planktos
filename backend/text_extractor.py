import fitz  # PyMuPDF
import docx2txt
import os

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file using PyMuPDF"""
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text("text") + "\n"
    return text.strip()

def extract_text_from_docx(file_path: str) -> str:
    """Extract text from a DOCX file"""
    return docx2txt.process(file_path).strip()

def extract_text_from_txt(file_path: str) -> str:
    """Extract text from a TXT file"""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def extract_text(file_path: str, content_type: str) -> str:
    """Route extraction based on file type"""
    if content_type == "application/pdf":
        return extract_text_from_pdf(file_path)
    elif content_type in [
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/msword"
    ]:
        return extract_text_from_docx(file_path)
    elif content_type == "text/plain":
        return extract_text_from_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {content_type}")
