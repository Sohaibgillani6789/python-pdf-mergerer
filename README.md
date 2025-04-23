# PDF Merger Application

## Setup Instructions

### 1. Install Python (Choose one method)

#### Method A: From Official Website (Recommended)
1. Download Python from [python.org](https://www.python.org/downloads/)
2. **Important:** During installation:
   - ✅ Check "Add Python to PATH"
   - ✅ Check "Install for all users"
3. Click "Install Now"
4. After installation, restart your computer

#### Method B: From Microsoft Store
If you see "Python was not found" message:
1. Open Microsoft Store
2. Search for "Python"
3. Install the latest version (e.g., Python 3.11)
4. After installation, restart your computer

#### Method C: Fix App Execution Aliases
If you still see the error:
1. Open Windows Settings
2. Go to Apps > Advanced app settings > App execution aliases
3. Turn OFF "App Installer" for both "python.exe" and "python3.exe"
4. Restart your computer

### 2. Verify Python Installation
Open a NEW Command Prompt and run:
```
python --version
```
If that doesn't work, try:
```
py --version
```
or
```
python3 --version
```

### 3. Install pip (if not already installed)
If pip is not recognized, try these steps:
1. Download get-pip.py:
   - Visit: https://bootstrap.pypa.io/get-pip.py
   - Save the file as get-pip.py
2. Open Command Prompt as Administrator
3. Navigate to the folder containing get-pip.py
4. Run:
   ```
   python get-pip.py
   ```

### 4. Install Dependencies
Once Python is working, run:
```
python -m pip install -r requirements.txt
```
or
```
py -m pip install -r requirements.txt
```

### 5. Run the Application
1. Open Command Prompt as Administrator
2. Navigate to your project folder:
```
cd c:\Users\sohai\Desktop\project
```
3. Run the application:
```
python app.py
```
4. If successful, you should see:
   - "Starting PDF Merger Application..."
   - "Server starting at http://127.0.0.1:5000"
5. Open your web browser and go to: http://127.0.0.1:5000

If you don't see any output:
- Make sure all project files exist in the correct location
- Try running with python3: `python3 app.py`
- Try running with py: `py app.py`
- Check if Flask is installed by running these commands:
  ```
  python -m pip list
  ```
  You should see Flask and other required packages in the list:
  ```
  Flask         2.0.1
  PyPDF2        3.0.1
  Werkzeug      2.0.1
  ```
  If packages are missing, run:
  ```
  python -m pip install -r requirements.txt
  ```
