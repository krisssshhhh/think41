import React, { createContext, useState } from "react";

// Create the context
export const ChatContext = createContext();

// Create provider
export const ChatProvider = ({ children }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const addMessage = (msg) => {
    setMessages((prev) => [...prev, msg]);
  };

  return (
    <ChatContext.Provider
      value={{ messages, addMessage, input, setInput, loading, setLoading }}
    >
      {children}
    </ChatContext.Provider>
  );
};