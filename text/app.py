from flask import Flask, render_template, request, send_file
import os
from scanner import scan_document
from werkzeug.utils import secure_filename
from summarizer import summarize_text


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        files = request.files.getlist('images')
        scanned_results = []

        for file in files:
            if file:
                filename = secure_filename(file.filename)
                upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(upload_path)

                scanned_path, extracted_text = scan_document(upload_path)

                if scanned_path:
                    scanned_results.append({
                        'scanned_img': scanned_path,
                        'extracted_text': extracted_text,
                        'filename': filename
                    })

        # Save all extracted text to a single downloadable file
        all_text = "\n\n".join([res['extracted_text'] for res in scanned_results])
        full_text_path = os.path.join(app.config['UPLOAD_FOLDER'], 'full_text.txt')
        with open(full_text_path, 'w', encoding='utf-8') as f:
            f.write(all_text)

        return render_template('upload.html', results=scanned_results, text_file='full_text.txt')
    return render_template('upload.html', results=None)

@app.route('/print/<filename>')
def print_document(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

@app.route('/summarize', methods=['POST'])
def summarize_route():
    full_text = request.form.get('full_text')
    summary = summarize_text(full_text)
    return render_template('summary.html', original=full_text, summary=summary)


if __name__ == '__main__':
    app.run(debug=True)
