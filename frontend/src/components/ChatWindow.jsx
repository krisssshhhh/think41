// components/ChatWindow.jsx
import React, { useState } from "react";
import MessageList from "./MessageList";
import UserInput from "./UserInput";
import "./ChatWindow.css";

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);

  const handleSend = (msgText) => {
    const userMsg = { sender: "user", text: msgText };
    setMessages((prev) => [...prev, userMsg]);

    // TODO: Call backend /api/chat
    const aiMsg = {
      sender: "ai",
      text: "Loading response from AI..." // placeholder
    };
    setMessages((prev) => [...prev, aiMsg]);
  };

  return (
    <div className="chat-window">
      <MessageList messages={messages} />
      <UserInput onSend={handleSend} />
    </div>
  );
};

export default ChatWindow;