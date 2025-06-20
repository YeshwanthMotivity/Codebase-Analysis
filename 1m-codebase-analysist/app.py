# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import shutil
import warnings

from easycontext_cpu.chunk import chunk_text
from easycontext_cpu.chunk_codebase import chunk_codebase
from easycontext_cpu.file_explorer import unzip_project
from easycontext_cpu.generate import run_rag_pipeline

# -------------------------------------
# App Config
# -------------------------------------
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max upload
CORS(app)
warnings.filterwarnings("ignore", category=FutureWarning)

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -------------------------------------
# Utility Functions
# -------------------------------------

EXCLUDE_DIRS = {'.git', '.venv', 'venv', '__pycache__', 'node_modules', '.idea'}
VALID_EXTENSIONS = {'.py', '.js', '.java', '.cpp', '.ts', '.html', '.css', '.c','.txt', '.ipynb'}

def get_filtered_file_paths(root_dir):
    valid_files = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            if os.path.splitext(file)[1] in VALID_EXTENSIONS:
                valid_files.append(os.path.join(root, file))
    return valid_files

# -------------------------------------
# Routes
# -------------------------------------
@app.route("/", methods=["POST"])
def ask():
    uploaded_file = request.files.get("file")
    question = request.form.get("question")

    if not uploaded_file or not question:
        return jsonify({"error": "Missing file or question"}), 400

    # Clear old files in uploads
    for f in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, f)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"❌ Could not delete old upload: {e}")

    filename = uploaded_file.filename.lower()
    saved_path = os.path.join(UPLOAD_FOLDER, filename)
    uploaded_file.save(saved_path)

    try:
        if filename.endswith(".zip"):
            # Unzip and automatically cleans temp_project inside unzip_project
            project_path = unzip_project(saved_path)

            # Collect valid code files only
            file_paths = get_filtered_file_paths(project_path)

            # Chunk the codebase files
            chunks = chunk_codebase(file_paths)

            # Delete the zip file after extracting
            os.remove(saved_path)

        else:
            # Handle plain .txt input
            with open(saved_path, "r", encoding="utf-8") as f:
                file_content = f.read()
            chunks = chunk_text(file_content)

        # Run RAG pipeline with the collected chunks
        answer = run_rag_pipeline("\n".join(chunks), question, token_limit=4000)

        return jsonify({"answer": answer})

    except Exception as e:
        print("🔥 Backend exception:", e)
        return jsonify({"error": f"Processing failed: {str(e)}"}), 500

# -------------------------------------
# Main
# -------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
