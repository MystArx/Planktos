from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

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
    """Recieve file,extract text and return"""

    if not file:
        raise HTTPException(status_code="400",detail="File upload failed")
    
    
    #TODO: pdf/tesseract logic


    try:
        content =await file.read()

        #TODO: EXTRACT TEXT
        simulated_extracted_text= f"Extracted text placeholder for '{file.filename}'"


        return{
            "filename":file.filename,
            "content_type":file.content_type,
            "extracted_text":simulated_extracted_text
        }
    except Exception as e:
        raise HTTPException(status_code="500",detail=f"File processing failed: {str(e)}")