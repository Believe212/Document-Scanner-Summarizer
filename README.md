# Document-Scanner-Summarizer

A Flask web application that allows users to upload document images, extract text using OCR, and generate summaries using NLP techniques.

## 🚀 Features
- Upload multiple images of documents.
- Automatically scan and extract text from each image.
- View scanned images alongside extracted text.
- Download the full extracted text as a `.txt` file.
- Summarize the extracted text in one click.

## 🛠 Tech Stack
- Python & Flask
- Tesseract OCR (via `scanner.py`)
- NLP Summarizer (via `summarizer.py`)
- HTML, CSS (Jinja templates)

## 📂 Project Structure
├── app.py
├── scanner.py
├── summarizer.py
├── templates/
│ ├── landing.html
│ ├── upload.html
│ └── summary.html
├── static/
│ └── uploads/

## 💻 Getting Started
1. Clone the repository:
   git clone https://github.com/your-username/document-scanner-summarizer.git
   cd document-scanner-summarizer
   
Install dependencies:
pip install -r requirements.txt

Run the app:
python app.py

📌 Note
Make sure Tesseract OCR is installed and accessible in your system PATH.
