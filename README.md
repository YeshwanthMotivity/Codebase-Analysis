# Codebase Analysis AI
A powerful RAG-based tool to analyze, understand, and chat with your entire codebase. Powered by **Qwen 2.5 Coder** and **Ollama**.

## 🚀 Features

- **Smart Context**: Upload a project (`.zip`) once, and the AI remembers the context for all subsequent questions.
- **RAG Architecture**: Uses Retrieval-Augmented Generation to find the exact code snippets relevant to your query.
- **Voice Interaction**: Ask questions via voice and listen to the AI's response.
- **Modern UI**: Clean, professional interface with Light/Dark mode.
- **Local Privacy**: Runs entirely locally using Ollama, keeping your code secure.


---
### 🧠 Architechture
![p1](https://github.com/user-attachments/assets/0712baf0-5a33-4d8c-8a5e-7579fad58186)

---
### 🛠️ Tech Stack

|        Layer       |       Technologies Used          |
| ------------------ | -------------------------------  |
| **Frontend**       | `React.js`                       |
| **Backend**        | `Flask`                          |
| **LLM Engine**     | `Qwen 2.5 Coder` (via Ollama)         |
| **Vector Search**  | `SentenceTransformers` (MiniLM)  |
| **Chunking**       | `Hugging Face Transformers`      |
| **Infrastructure** | `Ollama`                         |


## 📦 Installation

### Prerequisites
1.  **Python 3.10+**
2.  **Node.js** & **npm**
3.  **Ollama**: [Download Here](https://ollama.com/)
    -   Pull the model: `ollama pull qwen2.5-coder:7b`

### 1. Backend Setup
Navigate to the backend directory and install dependencies.

```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

Start the backend server:
```bash
python app.py
```
*Server runs on `http://127.0.0.1:5001`*

### 2. Frontend Setup
Navigate to the frontend directory.

```bash
cd frontend
npm install
npm start
```
*App runs on `http://localhost:3000`*

## 💡 Usage

1.  Open the web interface.
2.  Click **Select Project** and upload your codebase as a `.zip` file.
3.  Wait for the analysis to complete (Chunks & Indexing).
4.  Ask questions like *"How does the authentication flow work?"* or *"Explain App.js"*.


## 🙋‍♂️ Author

• Mentor / Manager: Mr. Venkata Ramana Sudhakar Polavarapu

• Mudimala Yeshwanth Goud

 🛠️ Passionate about AI/ML, NLP, RAG, Data Science, system programming, full-stack development, and intelligent assistant systems.

---
## 📬 Contact
For questions or collaboration, you can reach out at:

**Email 📧** : yeshwanth.mudimala@motivitylabs.com
