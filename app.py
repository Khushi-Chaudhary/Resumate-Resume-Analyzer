from flask import Flask, render_template, request, redirect, url_for
import os
from resume_analyzer import analyze_resume

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return 'No file part'
    file = request.files['resume']
    if file.filename == '':
        return 'No selected file'
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        feedback = analyze_resume(filepath)
        return render_template('result.html', feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
