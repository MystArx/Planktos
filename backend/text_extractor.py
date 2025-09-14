import fitz  # PyMuPDF
import docx2txt
import os

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract text from PDF bytes using PyMuPDF"""
    text = ""
    with fitz.open(stream=file_bytes, filetype="pdf") as pdf:
        for page in pdf:
            text += page.get_text("text") + "\n"
    return text.strip()

def extract_text_from_docx(file_bytes: bytes) -> str:
    """Extract text from DOCX bytes"""
    tmp_path = "temp_doc.docx"
    with open(tmp_path, "wb") as f:
        f.write(file_bytes)
    text = docx2txt.process(tmp_path)
    os.remove(tmp_path)
    return text.strip()

def extract_text_from_txt(file_bytes: bytes) -> str:
    """Extract text from TXT bytes"""
    return file_bytes.decode("utf-8").strip()

def extract_text(file_bytes: bytes, content_type: str) -> str:
    """Route extraction based on content type"""
    if content_type == "application/pdf":
        return extract_text_from_pdf(file_bytes)
    elif content_type in [
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/msword"
    ]:
        return extract_text_from_docx(file_bytes)
    elif content_type == "text/plain":
        return extract_text_from_txt(file_bytes)
    else:
        raise ValueError(f"Unsupported file type: {content_type}")
