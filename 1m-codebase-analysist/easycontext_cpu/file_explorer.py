import os
import zipfile
import shutil

# Folders to ignore
EXCLUDE_DIRS = {'__pycache__', '.git', 'node_modules', '.idea', '.vscode', '.venv', 'venv'}

# Valid extensions to allow
INCLUDE_EXTENSIONS = {'.py', '.js', '.ts', '.java', '.md', '.txt', '.json', '.html', '.css'}

def unzip_project(zip_path: str, extract_to: str = "./temp_project"):
    # Clean the temp_project directory first
    if os.path.exists(extract_to):
        shutil.rmtree(extract_to)
    os.makedirs(extract_to, exist_ok=True)

    # Extract the new zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    print(f"✅ Extracted zip to: {extract_to}")
    return extract_to

def get_filtered_file_paths(root_dir: str):
    file_paths = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            if any(file.endswith(ext) for ext in INCLUDE_EXTENSIONS):
                path = os.path.join(root, file)
                file_paths.append(path)
    print(f"📁 Total valid files: {len(file_paths)}")
    return file_paths
