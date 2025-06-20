💻 Codebase Analyst
Codebase Analyst is a GenAI-powered tool that helps developers understand and query complex codebases using natural language. It uses a Retrieval-Augmented Generation (RAG) pipeline and CodeLLaMA to extract and explain code from uploaded repositories intelligently.

🚀 Features
Natural Language Interaction – Ask questions about your codebase in plain English.

Context-Aware Answers – Answers are derived directly from your codebase.

Zipped Repository Uploads – Upload your codebase as a .zip file.

Intelligent File Filtering – Skips unnecessary folders like __pycache__, .git, node_modules, etc.

RAG Architecture – Combines retrieval and generation for accurate results.

🛠 Tech Stack
Layer	Technologies Used
Frontend	React.js – For building responsive UI
Backend	Flask – Lightweight Python server
LLM Engine	CodeLLaMA (via Ollama) – Code understanding
Vector Search	SentenceTransformers (MiniLM) – Semantic retrieval
Chunking	Hugging Face Transformers – Token-based splitting
Infrastructure	Ollama – Lightweight local LLM serving

✅ Prerequisites
🔧 Backend (Python)
Python: 3.9+

pip: For installing Python libraries

Git: For cloning the repo

Ollama: Local server for CodeLLaMA

⚠️ Important: Downgrade to Ollama v0.6.8 for compatibility with CodeLLaMA instruction-tuned models.

🧩 Frontend (React)
Node.js

npm

Basic React knowledge

🔍 Verify Installations
bash
Copy
Edit
python --version      # Should be 3.9+
pip --version
node --version
npm --version
ollama --version      # Should be v0.6.8
🗂 Project Structure
Copy
Edit
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
⚙️ Setup & Run Instructions
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/YeshwanthMotivity/Codebase-Analysist.git
cd 1M-CODEBASE-ANALYSIST/
2️⃣ Frontend Setup (React)
bash
Copy
Edit
cd easycontext-frontend
npm install
npm start
App runs on: http://localhost:3000

3️⃣ Ollama Setup
Downgrade Ollama to v0.6.8 (refer to official site/documentation)

Verify Version:

bash
Copy
Edit
ollama --version  # Should return ollama version 0.6.8
Pull & Run CodeLLaMA:

bash
Copy
Edit
ollama pull codellama:7b
ollama run codellama:7b
4️⃣ Backend Setup (Flask)
bash
Copy
Edit
# From project root
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
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

🔁 What Happens Behind the Scenes
Unzipping: Uploaded zip is extracted.

Filtering: Unwanted files are ignored.

Chunking: Code is split using token-based logic.

Embedding: Chunks embedded using MiniLM.

Retrieval: Relevant chunks fetched using cosine similarity + TF-IDF.

Prompt Building: A smart prompt is built.

Answer Generation: Prompt is sent to CodeLLaMA via Ollama.

Response: Final answer is displayed in a user-friendly format.

⏳ Response time depends on codebase size.

📦 Sample Output
pgsql
Copy
Edit
Q: What does the data_processor.py file do?
A: The file is responsible for preprocessing the input data before it is fed into the model. It handles missing values, feature encoding, and normalization.
🧾 License
This project is licensed under the MIT License. See LICENSE for details.
