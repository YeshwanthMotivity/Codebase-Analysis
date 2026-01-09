import os
from pathlib import Path
from multiprocessing import Pool, cpu_count
from .chunk import chunk_text

# Allow these code file types only
ALLOWED_EXTS = {".py", ".js", ".html", ".css", ".txt", ".md", ".ts", ".java", ".json"}
MAX_FILE_SIZE = 500 * 1024  # 500 KB

def load_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""

def chunk_single_file(path, max_tokens=1024):
    ext = Path(path).suffix.lower()
    if ext not in ALLOWED_EXTS:
        return []

    try:
        if os.path.getsize(path) > MAX_FILE_SIZE:
            print(f"[WARN] Skipped large file: {path}")
            return []
    except Exception as e:
        print(f"[ERROR] Error checking size for {path}: {e}")
        return []

    content = load_file(path)
    if not content.strip() or len(content) < 50:
        return []  # Skip empty or short files

    try:
        chunks = chunk_text(content, chunk_size=max_tokens, stride=max_tokens // 2)
        return [f"[{path}]\n{chunk}" for chunk in chunks]
    except Exception as e:
        print(f"[ERROR] Failed to chunk {path}: {e}")
        return []

def chunk_codebase(file_paths, max_tokens=1024):
    print(f"[INFO] Chunking {len(file_paths)} files using {cpu_count()} CPU cores...")
    args = [(path, max_tokens) for path in file_paths]

    with Pool(processes=cpu_count()) as pool:
        all_chunks_nested = pool.starmap(chunk_single_file, args)

    all_chunks = [chunk for sublist in all_chunks_nested for chunk in sublist]
    print(f"[SUCCESS] Done. Total chunks: {len(all_chunks)}")
    return all_chunks
