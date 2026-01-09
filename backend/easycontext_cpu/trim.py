from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-hf")

def trim_chunks(chunks, query, token_limit=16000):
    query_tokens = tokenizer.encode(query)
    max_context_tokens = token_limit - len(query_tokens) - 200  # buffer for prompt + answer

    selected_chunks = []
    current_tokens = 0

    for chunk in chunks:
        chunk_tokens = tokenizer.encode(chunk)
        if current_tokens + len(chunk_tokens) > max_context_tokens:
            break
        selected_chunks.append(chunk)
        current_tokens += len(chunk_tokens)

    return selected_chunks


