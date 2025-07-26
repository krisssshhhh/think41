// context/ChatContext.jsx
import React, { createContext, useState } from "react";

export const ChatContext = createContext();

export const ChatProvider = ({ children }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [sessions, setSessions] = useState([]); // ← 🆕 past sessions
  const [activeSession, setActiveSession] = useState(null); // ← 🆕

  const addMessage = (msg) => {
    setMessages((prev) => [...prev, msg]);
  };

  const switchSession = (sessionId) => {
    // Simulate fetching messages from DB using session ID
    const session = sessions.find((s) => s.id === sessionId);
    if (session) {
      setMessages(session.messages);
      setActiveSession(sessionId);
    }
  };

  const saveSession = () => {
    const newSession = {
      id: Date.now(),
      messages: [...messages],
    };
    setSessions((prev) => [newSession, ...prev]);
    setMessages([]);
    setActiveSession(newSession.id);
  };

  return (
    <ChatContext.Provider
      value={{
        messages,
        input,
        loading,
        sessions,
        activeSession,
        setInput,
        setLoading,
        addMessage,
        switchSession,
        saveSession,
      }}
    >
      {children}
    </ChatContext.Provider>
  );
};