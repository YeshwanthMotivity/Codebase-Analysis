# Codebase Analyst
 Codebase Analyst is a GenAI-powered tool that helps developers understand and query complex codebases using natural language. It uses a Retrieval-Augmented Generation (RAG) pipeline and CodeLLaMA to extract and  explain code from uploaded repositories intelligently.
 
---
### 🚀 Features
1. **Natural Language Interaction** – Ask questions about your codebase in plain English.
2. **Context-Aware Answers** – Answers are derived directly from your codebase.
3. **Zipped Repository Uploads** – Upload your codebase as a .zip file.
4. **Intelligent File Filtering** – Skips unnecessary folders like __pycache__, .git, node_modules, etc.
5. **RAG Architecture** – Combines retrieval and generation for accurate results.

---
### 🧠 Architechture
![p1](https://github.com/user-attachments/assets/0712baf0-5a33-4d8c-8a5e-7579fad58186)

---
### 🛠️ Tech Stack

|        Layer       |       Technologies Used          |
| ------------------ | -------------------------------  |
| **Frontend**       | `React.js`                       |
| **Backend**        | `Flask`                          |
| **LLM Engine**     | `CodeLLaMA` (via Ollama)         |
| **Vector Search**  | `SentenceTransformers` (MiniLM)  |
| **Chunking**       | `Hugging Face Transformers`      |
| **Infrastructure** | `Ollama`                         |

---
### ⚙️ How to Run
#### Prerequisites
• Backend (Python): Python 3.9+, pip, and Git.
• Frontend (React): Node.js and npm.
• Ollama: A local Ollama server is required to run CodeLLaMA. Important: You must downgrade to Ollama v0.6.8 for compatibility with the CodeLLaMA instruction-tuned models used in this project.

#### Verify Installations
• Make sure all required versions are correctly installed by running the following commands:
```
python --version   # Should be 3.9+
pip --version
node --version
npm --version
ollama --version   # Should be v0.6.8
```

#### Setup & Execution
• Clone the Repository
```
git clone https://github.com/YeshwanthMotivity/Codebase-Analysist.git
cd 1M-CODEBASE-ANALYSIST/

```
• Ollama Setup
First, downgrade Ollama to the required v0.6.8, then pull and run the CodeLLaMA model.
```
# Downgrade Ollama (refer to official documentation for your OS)
ollama pull codellama:7b
ollama run codellama:7b
```
• Frontend Setup (React)
In a new terminal, set up the frontend. The application will run on http://localhost:3000.
```
cd easycontext-frontend
npm install
npm start
```
• Backend Setup (Flask)
In a separate terminal, navigate to the project root and set up the Flask server. The server will run on http://127.0.0.1:5000.
```
python -m venv venv
venv\Scripts\activate   # For Windows
# source venv/bin/activate  # For macOS/Linux
pip install -r requirements.txt
python app.py
```
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
