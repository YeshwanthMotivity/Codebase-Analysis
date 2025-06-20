# Codebase Analyst
 Codebase Analyst is a GenAI-powered tool that helps developers understand and query complex codebases using natural language. It uses a Retrieval-Augmented Generation (RAG) pipeline and CodeLLaMA to extract and  explain code from uploaded repositories intelligently.

# Features
1. Natural Language Interaction – Ask questions about your codebase in plain English.
2. Context-Aware Answers – Answers are derived directly from your codebase.
3. Zipped Repository Uploads – Upload your codebase as a .zip file.
4. Intelligent File Filtering – Skips unnecessary folders like __pycache__, .git, node_modules, etc.
5. RAG Architecture – Combines retrieval and generation for accurate results.

# Tech Stack
Layer	Technologies Used
1. Frontend	React.js – For building responsive UI
2. Backend	Flask – Lightweight Python server
3. LLM Engine	CodeLLaMA (via Ollama) – Code understanding
4. Vector Search	SentenceTransformers (MiniLM) – Semantic retrieval
5. Chunking	Hugging Face Transformers – Token-based splitting
6. Infrastructure	Ollama – Lightweight local LLM serving

# Prerequisites
1. Backend (Python)
   Python: 3.9+
   pip: For installing Python libraries
   Git: For cloning the repo
   Ollama: Local server for CodeLLaMA
⚠️ Important: Downgrade to Ollama v0.6.8 for compatibility with CodeLLaMA instruction-tuned models.

2. Frontend (React)
   Node.js
   npm
   Basic React knowledge

3. Verify Installations
   python --version      # Should be 3.9+
   pip --version
   node --version
   npm --version
   ollama --version      # Should be v0.6.8

# Project Structure

📂 1M-CODEBASE-ANALYSIST/
│
├── 📂 easycontext_cpu/
│   ├── chunk.py
│   ├── chunkcodebase.py
│   ├── generate.py
│   ├── infer_model.py
│   ├── rerank.py
│   ├── retrieve_chunks.py
│   ├── trim.py
│
├── 📂 easycontext-frontend/
│   └── App.js


# Setup & Run Instructions

1️⃣ Clone the Repository

    git clone https://github.com/YeshwanthMotivity/Codebase-Analysist.git
    cd 1M-CODEBASE-ANALYSIST/

2️⃣ Frontend Setup (React)

    cd easycontext-frontend
    npm install
    npm start
    App runs on: http://localhost:3000

3️⃣ Ollama Setup

    Downgrade Ollama to v0.6.8 (refer to official site/documentation)
    Verify Version:
    ollama --version  # Should return ollama version 0.6.8

    Pull & Run CodeLLaMA:
    ollama pull codellama:7b
    ollama run codellama:7b

4️⃣ Backend Setup (Flask)

1. From project root
   python -m venv venv
2. Activate:
   venv\Scripts\activate
3. Install dependencies
   pip install -r requirements.txt
4. Run the server
5. python app.py
Flask runs on: http://127.0.0.1:5000

🧠 How to Use
📤 Upload Codebase
    Click on "Choose File" under "Upload a text file"
    Select your .zip codebase
    Only relevant files (like .py, .js, .html) will be processed
    
❓ Ask a Question
   Enter your question in plain English:
   "What is the primary purpose of the project and what components does it use?"
   "What does the transform module do?"
Click "Ask" to submit.

# 🔁 What Happens Behind the Scenes

1. Unzipping: Uploaded zip is extracted.
2. Filtering: Unwanted files are ignored.
3. Chunking: Code is split using token-based logic.
4. Embedding: Chunks embedded using MiniLM.
5. Retrieval: Relevant chunks fetched using cosine similarity + TF-IDF.
6. Prompt Building: A smart prompt is built.
7. Answer Generation: Prompt is sent to CodeLLaMA via Ollama.
8. Response: Final answer is displayed in a user-friendly format.

⏳ Response time depends on codebase size.

# 📬 Contact
For questions, feedback, or contributions:
📧 yeshwanth.mudimala@motivitylabs.com
