import os
import zipfile
import shutil
import time

# Folders to ignore
EXCLUDE_DIRS = {'__pycache__', '.git', 'node_modules', '.idea', '.vscode', '.venv', 'venv'}

# Valid extensions to allow
INCLUDE_EXTENSIONS = {'.py', '.js', '.ts', '.java', '.md', '.txt', '.json', '.html', '.css'}

def unzip_project(zip_path: str, extract_to: str = "./temp_project"):
    start_time = time.time()
    # Clean the temp_project directory first
    if os.path.exists(extract_to):
        shutil.rmtree(extract_to)
    os.makedirs(extract_to, exist_ok=True)

    # Extract the new zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    duration = time.time() - start_time
    print(f"[SUCCESS] [Unzip] Extracted project in {duration:.2f}s to: {extract_to}")
    return extract_to

def get_filtered_file_paths(root_dir: str):
    file_paths = []
    ignored_count = 0
    for root, dirs, files in os.walk(root_dir):
        # Filter directories in-place
        ignored_dirs = [d for d in dirs if d in EXCLUDE_DIRS]
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        if ignored_dirs:
            print(f"   [INFO] [FileExplorer] Ignoring folders: {ignored_dirs} in {root}")

        for file in files:
            if any(file.endswith(ext) for ext in INCLUDE_EXTENSIONS):
                path = os.path.join(root, file)
                file_paths.append(path)
            else:
                ignored_count += 1
                
    print(f"[INFO] [FileExplorer] Found {len(file_paths)} valid files. Ignored {ignored_count} other files.")
    return file_paths
