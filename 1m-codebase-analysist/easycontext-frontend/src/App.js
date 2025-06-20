import React, { useState } from "react";

const styles = {
  container: {
    maxWidth: 700,
    margin: "40px auto",
    fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
    backgroundColor: "#f9fafb",
    borderRadius: 8,
    padding: 30,
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
  },
  heading: {
    textAlign: "center",
    color: "#2c3e50",
    marginBottom: 30,
    fontWeight: "700",
  },
  formGroup: {
    marginBottom: 20,
  },
  label: {
    display: "block",
    fontWeight: "600",
    marginBottom: 8,
    color: "#34495e",
  },
  fileInput: {
    padding: "8px 12px",
    borderRadius: 5,
    border: "1px solid #ccc",
    width: "100%",
    boxSizing: "border-box",
  },
  textInput: {
    width: "100%",
    padding: "10px 12px",
    borderRadius: 5,
    border: "1px solid #ccc",
    fontSize: 16,
    boxSizing: "border-box",
  },
  button: {
    width: "100%",
    padding: "12px",
    borderRadius: 5,
    border: "none",
    backgroundColor: "#3498db",
    color: "#fff",
    fontSize: 18,
    fontWeight: "600",
    cursor: "pointer",
    transition: "background-color 0.3s ease",
  },
  buttonDisabled: {
    backgroundColor: "#95a5a6",
    cursor: "not-allowed",
  },
  errorText: {
    color: "#e74c3c",
    fontWeight: "600",
    marginTop: 10,
  },
  resultContainer: {
    marginTop: 30,
    padding: 20,
    backgroundColor: "#fff",
    borderRadius: 8,
    boxShadow: "0 2px 6px rgba(0,0,0,0.1)",
  },
  sectionTitle: {
    color: "#2c3e50",
    fontWeight: "700",
    marginBottom: 10,
  },
  answerParagraph: {
    whiteSpace: 'pre-wrap', // This is crucial for rendering newlines
    maxHeight: '400px',
    overflowY: 'auto',
  }
};

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  // Now, 'answer' will hold a single string or null
  const [answer, setAnswer] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setAnswer(null); // Clear previous answer

    if (!file || !question) {
      setError("Please upload a file and enter a question.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("question", question);

    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:5000/", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.statusText}`);
      }

      const data = await response.json();
      if (data.error) {
        setError(data.error);
      } else {
        // Filter out non-string elements
        const stringAnswers = data.answer.filter(item => typeof item === 'string');

        // Take only the first string answer if available
        if (stringAnswers.length > 0) {
          setAnswer(stringAnswers[0]);
        } else {
          setAnswer("No relevant answer found."); // Or handle as appropriate
        }
      }
    } catch (err) {
      setError("Failed to fetch answer: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>Ask a Question from Your Document Or Codebase</h1>

      <form onSubmit={handleSubmit}>
        <div style={styles.formGroup}>
          <label htmlFor="file" style={styles.label}>
            Upload a text file:
          </label>
          <input
            id="file"
            type="file"
            accept=".txt"
            style={styles.fileInput}
            onChange={(e) => setFile(e.target.files[0])}
            disabled={loading}
            required
          />
        </div>

        <div style={styles.formGroup}>
          <label htmlFor="question" style={styles.label}>
            Enter your question:
          </label>
          <input
            id="question"
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Type your question here..."
            style={styles.textInput}
            disabled={loading}
            required
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          style={{
            ...styles.button,
            ...(loading ? styles.buttonDisabled : {}),
          }}
        >
          {loading ? "Asking..." : "Ask"}
        </button>
      </form>

      {error && <p style={styles.errorText}>{error}</p>}

      {answer && ( // Check if there's an answer to display
        <div style={styles.resultContainer}>
          <h2 style={styles.sectionTitle}>Answer(s):</h2>
          <p style={styles.answerParagraph}>
            {answer}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;