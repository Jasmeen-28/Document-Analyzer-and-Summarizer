import fitz  
import re
from summarizer import Summarizer
from transformers import pipeline
import docx  
import os

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    
    if ext == '.pdf':
        doc = fitz.open(file_path)
        return "\n".join([page.get_text() for page in doc])
    
    elif ext == '.docx':
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    
    elif ext == '.txt':
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    
    else:
        raise ValueError("Unsupported file format. Please use .pdf, .docx, or .txt.")

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extractive_summary(text, num_sentences=5):
    model = Summarizer()
    full_summary = model(text, min_length=50, max_length=150)
    sentences = full_summary.split('. ')
    return '. '.join(sentences[:num_sentences]) + '.'

def abstractive_summary(text, max_length=250, min_length=50):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
