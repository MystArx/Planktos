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
async def create_upload_file(file: UploadFile=File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="File upload failed")

    try:
        content = await file.read()
        extracted_text = extract_text(content, file.content_type)
        simplified_text = simplify_legal_text(extracted_text)

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "extracted_text": extracted_text[:500],  # preview text
            "simplified_text": simplified_text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File processing failed: {str(e)}")
