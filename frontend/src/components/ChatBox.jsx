import { useState } from "react";
import { askQuestion } from "../api";

export default function ChatBox() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleAsk = async () => {
    const res = await askQuestion(question);
    setAnswer(res.data.answer);
  };

  return (
    <div>
      <h3>Ask your document</h3>

      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask something..."
      />

      <button onClick={handleAsk}>
        Ask
      </button>

      <pre class="message" >{answer}</pre>
    </div>
  );
}