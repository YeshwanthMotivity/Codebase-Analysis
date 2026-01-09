import React, { useState, useRef, useEffect } from "react";
import ReactMarkdown from 'react-markdown';
import "./App.css";

function App() {
  // ... existing code ...

  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [processingStep, setProcessingStep] = useState(0);

  // New States
  const [contextLoaded, setContextLoaded] = useState(false); // True if backend has cached project
  const [theme, setTheme] = useState('light');
  const [isListening, setIsListening] = useState(false);

  // Track if currently speaking to toggle button
  const [isSpeaking, setIsSpeaking] = useState(false);

  const chatEndRef = useRef(null);

  // --- THEME TOGGLE ---
  useEffect(() => {
    document.body.setAttribute('data-theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  };

  // --- AUTO SCROLL ---
  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };
  useEffect(() => { scrollToBottom(); }, [chatHistory, loading]);

  // --- LOADING SIMULATION ---
  useEffect(() => {
    let interval;
    if (loading) {
      setProcessingStep(0);
      interval = setInterval(() => {
        setProcessingStep((prev) => (prev < 3 ? prev + 1 : prev));
      }, 4000);
    }
    return () => clearInterval(interval);
  }, [loading]);

  // --- VOICE INPUT (STT) ---
  const handleVoiceInput = () => {
    if (!('webkitSpeechRecognition' in window)) {
      alert("Voice input is not supported in this browser. Try Chrome.");
      return;
    }
    const recognition = new window.webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.lang = 'en-US';

    recognition.onstart = () => setIsListening(true);
    recognition.onend = () => setIsListening(false);

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setQuestion(transcript);
    };

    recognition.start();
  };

  // --- VOICE OUTPUT (TTS) ---
  const speakText = (text) => {
    if ('speechSynthesis' in window) {
      // If already speaking, cancel it (Stop)
      if (window.speechSynthesis.speaking) {
        window.speechSynthesis.cancel();
        setIsSpeaking(false);
        return;
      }

      // Otherwise start speaking
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.pitch = 1;
      utterance.rate = 1;

      utterance.onend = () => setIsSpeaking(false);
      utterance.onerror = () => setIsSpeaking(false);

      setIsSpeaking(true);
      window.speechSynthesis.speak(utterance);
    }
  };

  // --- RESET / RE-ANALYZE ---
  const handleReset = () => {
    setContextLoaded(false);
    setFile(null);
    setChatHistory([]);
    setQuestion("");
    // Backend cache persists but will be overwritten on next upload
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!question) return;

    // UI Update
    const newHistory = [...chatHistory, { role: "user", content: question }];
    setChatHistory(newHistory);
    const currentQuestion = question;
    setQuestion("");
    setLoading(true);

    const formData = new FormData();

    // Only append file if we are in "Upload Mode" (not context loaded yet)
    if (!contextLoaded && file) {
      formData.append("file", file);
    }

    formData.append("question", currentQuestion);

    try {
      const response = await fetch("http://127.0.0.1:5001/", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) throw new Error(`Server error: ${response.statusText}`);

      const data = await response.json();

      let botAnswer = "No relevant answer found.";
      if (data.error) {
        botAnswer = `Error: ${data.error}`;
      } else if (data.answer) {
        botAnswer = typeof data.answer === 'string' ? data.answer : JSON.stringify(data.answer);
      }

      setChatHistory((prev) => [...prev, { role: "bot", content: botAnswer }]);

      // If successful response and we were in upload mode, mark context as loaded
      if (!contextLoaded && !data.error) {
        setContextLoaded(true);
      }

    } catch (err) {
      setChatHistory((prev) => [...prev, { role: "bot", content: `Connection failed: ${err.message}` }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="app-header">
        <div className="header-content">
          <div>
            <h1 className="app-title">Codebase Analysis</h1>
            <p className="app-subtitle">Powered by Qwen 2.5 Coder & RAG</p>
          </div>

          <div className="header-controls">
            <button onClick={toggleTheme} className="text-btn" title="Toggle Theme">
              {theme === 'light' ? 'Dark Mode' : 'Light Mode'}
            </button>
            {contextLoaded && (
              <button onClick={handleReset} className="text-btn" title="Re-analyze / New Project">
                Re-analyze
              </button>
            )}
          </div>
        </div>
      </header>

      <main className="main-card">
        {/* VIEW 1: EMPTY STATE / WELCOME (Only if no context and no history) */}
        {!contextLoaded && chatHistory.length === 0 && !loading && (
          <div className="processing-container">
            <h3>Start Analysis</h3>
            <p style={{ color: 'var(--text-muted)', marginBottom: 20 }}>Upload a project (.zip) to begin smart context analysis.</p>

            <label className="file-upload-box">
              <input
                type="file"
                onChange={(e) => setFile(e.target.files[0])}
                accept=".zip,.txt,.py,.js,.java,.cpp,.ts,.html,.css"
              />
              <span className="upload-text">{file ? file.name : "Select Project (.zip)"}</span>
            </label>
          </div>
        )}

        {/* VIEW 2: CHAT INTERFACE (Show if history exists or loading) */}
        {(chatHistory.length > 0 || loading) && (
          <div className="chat-window">
            {chatHistory.map((msg, index) => (
              <div key={index} className={`message ${msg.role}`}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 5, fontSize: '0.8rem', opacity: 0.7 }}>
                  <strong>{msg.role === 'user' ? 'YOU' : 'ASSISTANT'}</strong>
                  {msg.role === 'bot' && (
                    <button onClick={() => speakText(msg.content)} className="speak-link" title="Read Aloud or Stop">
                      {isSpeaking ? "Stop" : "Read Aloud"}
                    </button>
                  )}
                </div>
                <div className="markdown-content">
                  <ReactMarkdown>{msg.content}</ReactMarkdown>
                </div>
              </div>
            ))}

            {loading && (
              <div className="processing-container" style={{ minHeight: '200px', padding: 20 }}>
                <div className="pulse-dot"></div>
                <ul className="steps-list">
                  <li className={`step-item ${processingStep >= 0 ? 'active' : ''}`}>
                    {contextLoaded ? "Consulting Context..." : "Analyzing Project..."}
                  </li>
                  <li className={`step-item ${processingStep >= 1 ? 'active' : ''}`}>
                    Finding Relevant Code...
                  </li>
                  <li className={`step-item ${processingStep >= 2 ? 'active' : ''}`}>
                    Generating Answer...
                  </li>
                </ul>
              </div>
            )}
            <div ref={chatEndRef} />
          </div>
        )}

        <form className="input-dock" onSubmit={handleSubmit}>
          {/* HIDE File Upload if Context is Loaded */}
          {!contextLoaded && (
            <div className="mini-file-indicator" title={file ? file.name : "No file selected"}>
              {file ? 'File Selected' : 'No File'}
            </div>
          )}

          <input
            className="main-input"
            type="text"
            placeholder={!contextLoaded && !file ? "Upload a file first..." : "Ask a question..."}
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            disabled={loading || (!file && !contextLoaded)}
          />

          <button type="button" className="action-btn icon-only" onClick={handleVoiceInput} disabled={loading || isListening} title="Voice Input">
            {isListening ? 'Listening...' : 'Voice'}
          </button>

          <button type="submit" className="action-btn" disabled={loading || !question || (!file && !contextLoaded)}>
            Send
          </button>
        </form>
      </main>
    </div>
  );
}

export default App;