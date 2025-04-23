# flask-pdf-merger

This project is a Flask application that allows users to upload multiple PDF files and merge them into a single PDF document. 

## Project Structure

```
flask-pdf-merger
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── script.js
│   └── templates
│       └── index.html
├── .gitignore
├── Procfile
├── README.md
├── app.py
├── requirements.txt
└── runtime.txt
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/flask-pdf-merger.git
   cd flask-pdf-merger
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Upload multiple PDF files using the provided form on the main page.
- Click the submit button to merge the selected PDF files.
- The merged PDF will be downloaded automatically.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.