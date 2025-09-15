# Codebase Analyst
 Codebase Analyst is a GenAI-powered tool that helps developers understand and query complex codebases using natural language. It uses a Retrieval-Augmented Generation (RAG) pipeline and CodeLLaMA to extract and  explain code from uploaded repositories intelligently.
 
---
### Features
1. **Natural Language Interaction** – Ask questions about your codebase in plain English.
2. **Context-Aware Answers** – Answers are derived directly from your codebase.
3. **Zipped Repository Uploads** – Upload your codebase as a .zip file.
4. **Intelligent File Filtering** – Skips unnecessary folders like __pycache__, .git, node_modules, etc.
5. **RAG Architecture** – Combines retrieval and generation for accurate results.

---
### Architechture
![p1](https://github.com/user-attachments/assets/0712baf0-5a33-4d8c-8a5e-7579fad58186)

---
### Tech Stack

|        Layer       |       Technologies Used          |
| ------------------ | -------------------------------  |
| **Frontend**       | `React.js`                       |
| **Backend**        | `Flask`                          |
| **LLM Engine**     | `CodeLLaMA` (via Ollama)         |
| **Vector Search**  | `SentenceTransformers` (MiniLM)  |
| **Chunking**       | `Hugging Face Transformers`      |
| **Infrastructure** | `Ollama`                         |

---
### Prerequisites
**1. Backend (Python)**
   1. Python: 3.9+
   2. pip: For installing Python libraries
   3. Git: For cloning the repo
   4. Ollama: Local server for CodeLLaMA
   5. ⚠️ Important: Downgrade to Ollama v0.6.8 for compatibility with CodeLLaMA instruction-tuned models.

**2. Frontend (React)**
   1. Node.js
   2. npm
   3. Basic React knowledge

**3. Verify Installations**
   1. python --version      # Should be 3.9+
   2. pip --version
   3. node --version
   4. npm --version
   5. ollama --version      # Should be v0.6.8
      
---
### Project Structure

```
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
```
---

### Setup & Run Instructions

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

---

### 🧠 How to Use
1. 📤 Upload Codebase
    1. Click on "Choose File" under "Upload a text file"
    2. Select your .zip codebase (Only relevant files (like .py, .js, .html) will be processed)
    
2. ❓ Ask a Question
   1. Enter your question in plain English:
      1. "What is the primary purpose of the project and what components does it use?"
      2. "What does the transform module do?"
   2. Click "Ask" to submit.

---

### 🔁 What Happens Behind the Scenes

1. Unzipping: Uploaded zip is extracted.
2. Filtering: Unwanted files are ignored.
3. Chunking: Code is split using token-based logic.
4. Embedding: Chunks embedded using MiniLM.
5. Retrieval: Relevant chunks fetched using cosine similarity + TF-IDF.
6. Prompt Building: A smart prompt is built.
7. Answer Generation: Prompt is sent to CodeLLaMA via Ollama.
8. Response: Final answer is displayed in a user-friendly format.

⏳ Response time depends on codebase size.

---
### 📬 Contact
For questions, feedback, or contributions:
📧 yeshwanth.mudimala@motivitylabs.com
