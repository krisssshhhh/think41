import React, { useContext } from "react";
import { ChatContext } from "../context/ChatContext";

const UserInput = () => {
  const { input, setInput, addMessage, setLoading } = useContext(ChatContext);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    // Add user's message
    const userMessage = { sender: "user", text: input };
    addMessage(userMessage);
    setInput("");
    setLoading(true);

    // Send request to backend
    const response = await fetch("http://localhost:8000/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: "krish", message: input }),
    });

    const data = await response.json();
    const aiMessage = { sender: "ai", text: data.ai_response };
    addMessage(aiMessage);
    setLoading(false);
  };

  return (
    <form className="user-input" onSubmit={handleSubmit}>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type a message..."
      />
      <button type="submit">Send</button>
    </form>
  );
};

export default UserInput;