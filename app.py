from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.requests import Request
import shutil
import os
from fastapi.templating import Jinja2Templates
from transformers import pipeline
from analyzer import extract_text_from_file, clean_text, extractive_summary

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

templates = Jinja2Templates(directory="templates")

abstractive_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def abstractive_summary(text, max_length=150, min_length=30):
    if len(text) > 2000:
        text = text[:2000]
    summary = abstractive_pipeline(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze/")
async def analyze_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        text = extract_text_from_file(file_path)
        cleaned_text = clean_text(text)

        ext_summary = extractive_summary(cleaned_text)
        abs_summary = abstractive_summary(cleaned_text)

        return JSONResponse({
            "extractive_summary": ext_summary,
            "abstractive_summary": abs_summary
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

    finally:
        os.remove(file_path)
