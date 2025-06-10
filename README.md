# 📄 File Summarizer Web App

This is a **FastAPI**-based web application that allows users to upload `.pdf`, `.docx`, or `.txt` files and get both **extractive** and **abstractive summaries** using state-of-the-art NLP models.
![image](https://github.com/user-attachments/assets/e1fb7ddd-31a9-4d17-b78a-3ee0f3136184)

![image](https://github.com/user-attachments/assets/2b7ce913-17b1-4a25-a04d-b489606371be)



## ✨ Features

- ✅ Upload and summarize `.pdf`, `.docx`, or `.txt` files
- ✅ Extractive summarization using `bert-extractive-summarizer`
- ✅ Abstractive summarization using Hugging Face's `facebook/bart-large-cnn`
- ✅ Clean and efficient FastAPI backend
- ✅ Jinja2 templated frontend interface

## 🚀 Tech Stack

- **Backend:** FastAPI
- **Frontend:** HTML (Jinja2 templates)
- **NLP Models:** 
  - Extractive: `bert-extractive-summarizer`
  - Abstractive: `facebook/bart-large-cnn` via Hugging Face Transformers
- **File Parsing:** 
  - PDFs via `PyMuPDF (fitz)`
  - Word Docs via `python-docx`
  - Text Files via Python's built-in `open()`

## 🏁 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/file-summarizer-app.git
   cd file-summarizer-app

2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    # On Windows use `venv\Scripts\activate`

3. **Run the app**
    uvicorn main:app --reload
   
4. **Open your browser**
    http://127.0.0.1:8000/
   



