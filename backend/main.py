from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from text_extractor import extract_text
from llm_calls import simplify_legal_text

load_dotenv()

app=FastAPI()

origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    """Check Backend Endpoint"""
    return{"status":"success","message":"Backend up and running"}



@app.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    """Receive file, extract text, simplify, and return result"""

    if not file:
        raise HTTPException(status_code=400, detail="File upload failed")

    try:
        # Step 1: Read file content
        content = await file.read()

        # Step 2: Extract raw text (PDF, DOCX, TXT supported)
        extracted_text = extract_text_from_file(content, file.filename)

        if not extracted_text.strip():
            raise HTTPException(status_code=422, detail="No text could be extracted from file")

        # Step 3: Send to Gemini for simplification
        simplified_text = simplify_legal_text(extracted_text)

        # Step 4: Return response
        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "extracted_text": extracted_text[:1000],  # limit preview
            "simplified_text": simplified_text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File processing failed: {str(e)}")