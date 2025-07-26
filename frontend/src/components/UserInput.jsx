import React, { useState, useContext } from "react";
import { ChatContext } from "../context/ChatContext";
import { sendMessageToBot } from "../services/api";

export default function UserInput() {
  const [input, setInput] = useState("");
  const { userId, addMessage, setLoading } = useContext(ChatContext);

  const handleSend = async () => {
    if (!input.trim()) return;
    addMessage({ sender: "user", text: input });
    setLoading(true);
    try {
      const res = await sendMessageToBot(userId, input);
      addMessage({ sender: "bot", text: res.ai_response });
    } catch (err) {
      addMessage({ sender: "bot", text: `❌ ${err.message}` });
    } finally {
      setLoading(false);
      setInput("");
    }
  };

  return (
    <div className="user-input">
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyPress={(e) => e.key === "Enter" && handleSend()}
        placeholder="Type your message..."
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
}