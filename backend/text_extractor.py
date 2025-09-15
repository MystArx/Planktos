# text_extractor.py
import fitz  # PyMuPDF
import docx2txt
import os
import tempfile
from PIL import Image
import pytesseract
import io


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract text from a PDF file (bytes).
    Falls back to OCR if no text is found on a page.
    """
    text_blocks = []
    try:
        with fitz.open(stream=file_bytes, filetype="pdf") as pdf:
            for page in pdf:
                page_text = page.get_text("text")

                # If page has digital text, use it
                if page_text.strip():
                    text_blocks.append(page_text)
                else:
                    # Fallback to OCR for scanned page
                    pix = page.get_pixmap(dpi=300)
                    img = Image.open(io.BytesIO(pix.tobytes("png")))
                    ocr_text = pytesseract.image_to_string(img, lang="eng")
                    text_blocks.append(ocr_text)

    except Exception as e:
        raise ValueError(f"Error extracting text from PDF: {e}")

    return "\n".join(text_blocks).strip()


def extract_text_from_docx(file_bytes: bytes) -> str:
    """Extract text from a DOCX file (bytes)."""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            tmp.write(file_bytes)
            tmp_path = tmp.name

        text = docx2txt.process(tmp_path)
    except Exception as e:
        raise ValueError(f"Error extracting text from DOCX: {e}")
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    return (text or "").strip()


def extract_text_from_txt(file_bytes: bytes) -> str:
    """Extract text from a TXT file (bytes)."""
    try:
        return file_bytes.decode("utf-8", errors="ignore").strip()
    except Exception as e:
        raise ValueError(f"Error extracting text from TXT: {e}")


def extract_text(file_bytes: bytes, content_type: str) -> str:
    """Detect file type and extract text accordingly."""
    if content_type == "application/pdf":
        return extract_text_from_pdf(file_bytes)

    elif content_type in (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/msword",
    ):
        return extract_text_from_docx(file_bytes)

    elif content_type == "text/plain":
        return extract_text_from_txt(file_bytes)

    else:
        raise ValueError(f"Unsupported file type: {content_type}")