from flask import render_template, request, flash, send_file
from . import app
from PyPDF2 import PdfMerger
import os
import tempfile

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'files[]' not in request.files:
            flash('No files selected')
            return render_template('index.html')
        
        files = request.files.getlist('files[]')
        if not files or files[0].filename == '':
            flash('No files selected')
            return render_template('index.html')

        merger = PdfMerger()
        temp_dir = tempfile.mkdtemp()
        output_path = os.path.join(temp_dir, 'merged.pdf')

        try:
            for file in files:
                if file and allowed_file(file.filename):
                    merger.append(file)
                
            merger.write(output_path)
            merger.close()
            return send_file(output_path, as_attachment=True, download_name='merged.pdf')
        except Exception as e:
            flash('Error merging PDFs')
            return render_template('index.html')

    return render_template('index.html')