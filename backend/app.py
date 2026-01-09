# app.py

import sys
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
# Global Cache
PROJECT_CACHE = {
    "filename": None,
    "chunks": []
}

@app.route("/", methods=["POST"])
def ask():
    global PROJECT_CACHE
    
    try:
        # Check if a file is uploaded
        uploaded_file = request.files.get("file")
        question = request.form.get("question")

        if not question:
            return jsonify({"error": "Missing question"}), 400

        # CASE A: New Project Upload
        if uploaded_file:
            print("[INFO] New file upload detected. Processing...")
            
            # Clear old files in uploads
            for f in os.listdir(UPLOAD_FOLDER):
                file_path = os.path.join(UPLOAD_FOLDER, f)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(f"[ERROR] Could not delete old upload: {e}")

            filename = uploaded_file.filename.lower()
            saved_path = os.path.join(UPLOAD_FOLDER, filename)
            uploaded_file.save(saved_path)

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

            # UPDATE CACHE
            PROJECT_CACHE["filename"] = filename
            PROJECT_CACHE["chunks"] = chunks
            print(f"[SUCCESS] Cached {len(chunks)} chunks for {filename}")
        
        # CASE B: Follow-up Question (No File)
        else:
            print("[INFO] processing follow-up question using cached context...")
            chunks = PROJECT_CACHE["chunks"]
            if not chunks:
                return jsonify({"error": "No project loaded. Please upload a file first."}), 400

        # Run RAG pipeline with the chunks (either fresh or cached)
        # It returns (answer_str, prompt_str, debug_dict)
        answer, prompt, pipeline_debug = run_rag_pipeline("\n".join(chunks), question, token_limit=4000)

        # Merge pipeline debug info with cache info
        final_debug = {
            "cached_file": PROJECT_CACHE["filename"],
            "total_chunks": len(chunks),
            **pipeline_debug
        }

        return jsonify({
            "answer": answer,
            "debug_info": final_debug
        })

    except Exception as e:
        print("[ERROR] Backend exception:", e)
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Processing failed: {str(e)}"}), 500

# -------------------------------------
# Main
# -------------------------------------
if __name__ == "__main__":
    # Force unbuffered output
    sys.stdout.reconfigure(encoding='utf-8')
    
    print("[INFO] Starting Flask server on port 5000...")
    app.run(debug=False, host='0.0.0.0', port=5001)
