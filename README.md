# Codebase Analyst
Codebase Analyst is a GenAI-powered tool designed to help developers understand and query complex codebases using natural language. It leverages a Retrieval-Augmented Generation (RAG) approach and the CodeLLaMA language model to allow users to upload a zipped code repository and ask questions about it. The system acts as a technical expert, intelligently filtering, chunking, semantically indexing, and retrieving relevant code snippets to generate context-aware answers.

Features

Natural Language Interaction: Ask questions about your codebase in plain English.

Context-Aware Answers: The system provides answers derived contextually from your actual codebase and specific to your query.

Support for Zipped Repositories: Upload your entire codebase as a .zip file.

Intelligent Processing: Automatically filters out unwanted folders (e.g., __pycache__, .git, node_modules).

Retrieval-Augmented Generation (RAG): Utilizes a RAG pipeline for robust answer generation.


Tech Stack

The Codebase Analyst project is built with the following technologies:

Layer	Technologies Used

Frontend	React.js – for building a responsive and interactive UI 

Backend	Flask – lightweight Python server to handle inference and logic 

LLM Engine	CodeLLaMA (via Ollama) – for natural language code understanding 

Vector Search	SentenceTransformers (MiniLM) – for semantic similarity retrieval 

Chunking	Hugging Face Transformers – for token-based document chunking 

Infrastructure	Ollama – local lightweight model serving 

Prerequisites

Before setting up the Codebase Analyst project, ensure your system meets the following requirements:

Backend Requirements (Python Environment)
Python: 3.9+ 
pip: For managing and installing Python libraries 
Git: For cloning the project repository 
Ollama: Local LLM server used to run the CodeLLaMA model 
Important Note: Ollama version 0.6.8 is required for compatibility with instruction-tuned variants of CodeLLaMA. You must downgrade Ollama to version 0.6.8.


CodeLLaMA 7B: The LLM used for generating code explanations.
Frontend Requirements (React Environment)
Node.js: Required to run the React development server 
npm: Node package manager for installing dependencies 
Basic React Knowledge: Useful for modifying or debugging the frontend 

Verify Your Installations

You can verify your installations using the following commands:

python --version      # Should be 3.9+
pip --version
node --version
npm --version
ollama --version      # Should be v0.6.8

Project Structure

The project has the following folder layout:

📂 1M-CODEBASE-ANALYSIST
	 |
📂  easycontext_cpu/
   ├── chunk.py
   ├── chunkcodebase.py
   ├── generate.py
   ├── infer_model.py
   ├── rerank.py
   ├── retrieve_chunks.py
   ├── trim.py
📂  easycontext-frontend/
   └── App.js


Setup and Running the Application

1. Download the Project
   
You can either clone the repository or download the zip file from the GitHub Repository.


git clone https://github.com/YeshwanthMotivity/Codebase-Analysist.git

cd 1M-CODEBASE-ANALYSIST/ # Navigate to the main project directory if you cloned it

2. Frontend Setup
   
Open Project in VS Code: Launch VS Code and open the 1m-codebase-analysist folder.

Open Terminal: Go to Terminal > New Terminal and ensure the shell is set to Command Prompt (cmd).
Navigate to Frontend Directory:
cd easycontext-frontend 
Install React Dependencies:

npm install 

Start the React Development Server:

npm start
The app will run on http://localhost:3000.

3. Ollama Setup
   
Downgrade Ollama: If your Ollama version is not 0.6.8, download and run the installer for Ollama v0.6.8 from the provided link in the documentation. This will automatically downgrade your Ollama.

Verify Ollama Version: Open Command Prompt (CMD) and run:

ollama --version

# Output should be: ollama version 0.6.8 

Pull and Run CodeLLaMA Model:

ollama pull codellama:7b 

ollama run codellama:7b 

4. Backend Setup
   
Open Backend Folder in VS Code: If not already open, go to File > Open Folder and select the 1m-codebase-analysist folder.

Open Terminal: Click on Terminal > New Terminal to open the integrated terminal.

Create and Activate Virtual Environment (Recommended):

python -m venv venv

# Windows: venv\Scripts\activate 

# Linux/macOS: source venv/bin/activate 

Install Required Packages:

pip install -r requirements.txt 

Start the Flask Server:

python app.py 

The Flask app will typically run at http://127.0.0.1:5000.

How to Use the Codebase Analyst Web Interface
Upload Your Codebase:
Click on the "Choose File" button under "Upload a text file".
Select a .zip file containing your codebase or documentation.
Ensure the .zip includes only relevant source files (e.g., .py, .js, .html). Unwanted folders like __pycache__, .git, node_modules, etc., will be automatically excluded.
Ask a Question:

Enter your natural language question in the input field. This can be anything about the uploaded codebase.
Example questions:
"What is the primary purpose of the (project name) and what main components does it use to achieve its goal?" 
"What does transform module do in the project?" 

Click Ask:

After uploading the codebase and entering your question, click the "Ask" button.
A "Asking..." loading state will appear, indicating that the backend is processing your request.
Processing Your Request:

The backend will execute its Retrieval-Augmented Generation (RAG) pipeline. This involves: 
Unzipping and filtering valid files 
Chunking code using tokenization 
Embedding chunks using MiniLM for semantic similarity 
Ranking results using TF-IDF and cosine similarity 
Constructing a prompt and querying the CodeLLaMA model using Ollama 
Returning a clean, concise, and contextual answer 
Note: Response time may vary depending on the size of the codebase.
Answer Generated:

Once processing completes, the loading spinner will disappear, and a neatly formatted "Answer(s)" section will appear below the form.
The output will consist of a concise explanation or answer related to your codebase, context fetched from the most relevant files and code snippets, and a user-friendly text display.
