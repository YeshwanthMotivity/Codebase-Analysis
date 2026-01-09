
# easycontext_cpu/rag.py

from easycontext_cpu.chunk import chunk_text
from easycontext_cpu.retrieve_chunks import get_top_k_chunks
from easycontext_cpu.rerank import rerank_chunks
from easycontext_cpu.trim import trim_chunks
from easycontext_cpu.infer_model import generate_answer

def hybrid_retrieve(query, chunks, k=5):
    sem_chunks = get_top_k_chunks(query, chunks, k=10)
    return rerank_chunks(sem_chunks, query, top_k=k)

def run_rag_pipeline(text: str, query: str, token_limit: int = 16000, top_k: int = 5, use_codellama=False):
    print("[INFO] [RAG] Starting pipeline. Chunking input...")
    chunks = chunk_text(text, chunk_size=300, stride=200)

    print(f"[INFO] [RAG] Retrieving top {top_k} chunks from {len(chunks)} total chunks...")
    top_chunks = hybrid_retrieve(query, chunks, k=top_k)

    print(f"[INFO] [RAG] Trimming chunks to fit {token_limit} tokens...")
    trimmed = trim_chunks(top_chunks, query, token_limit=token_limit)
    print(f"   [INFO] [RAG] Final context has {len(trimmed)} chunks.")

    print("[INFO] [RAG] Generating answer from model...")
    answer = generate_answer(query, trimmed)
    prompt = "\n".join(trimmed)
    
    debug_info = {
        "stage_logs": [
             f"Chunked into {len(chunks)} parts",
             f"Retrieved top {top_k}",
             f"Trimmed to {len(trimmed)} final chunks"
        ],
        "chunks_before_retrieval_count": len(chunks),
        "top_chunks_count": len(top_chunks),
        "trimmed_chunks_count": len(trimmed)
    }
    return answer, prompt, debug_info

