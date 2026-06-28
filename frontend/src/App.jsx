import UploadBox from "./components/UploadBox";
import ChatBox from "./components/ChatBox";
import "./App.css";

function App() {
  return (
    <div className="app">
      {/* SIDEBAR */}
      <aside className="sidebar">
        <div className="logo">
          <h2>📄 AI Docs</h2>
          <p>Document Assistant</p>
        </div>

        <div className="sidebar-section">
          <h4>Upload PDF</h4>
          <UploadBox />
        </div>
      </aside>

      {/* MAIN */}
      <main className="main">
        <header className="topbar">
          <h1>Ask your document</h1>
          <p>Upload a PDF and chat with it using AI</p>
        </header>

        <div className="chat-container">
          <ChatBox />
        </div>
      </main>
    </div>
  );
}

export default App;