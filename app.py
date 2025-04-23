from flask import Flask, render_template, request, send_file, flash
from werkzeug.utils import secure_filename
from PyPDF2 import PdfMerger
import os
import tempfile

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flashing messages

# Create uploads directory if it doesn't exist
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if files were uploaded
        if 'files[]' not in request.files:
            flash('No files selected', 'error')
            return render_template('index.html')
        
        files = request.files.getlist('files[]')
        
        # Check if any file was selected
        if not files or files[0].filename == '':
            flash('No files selected', 'error')
            return render_template('index.html')

        try:
            merger = PdfMerger()
            
            # Create a temporary file for the merged PDF
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf', dir=UPLOAD_FOLDER) as tmp_file:
                output_path = tmp_file.name
                
                # Add each PDF to the merger
                for file in files:
                    if file and file.filename.lower().endswith('.pdf'):
                        merger.append(file)
                
                # Write the merged PDF to the temporary file
                merger.write(output_path)
                merger.close()
                
                # Send the file to the user
                return send_file(
                    output_path,
                    as_attachment=True,
                    download_name='merged.pdf'
                )
                
        except Exception as e:
            flash(f'Error merging PDFs: {str(e)}', 'error')
            return render_template('index.html')
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
