import React, { createContext, useState } from "react";

export const ChatContext = createContext();

export const ChatProvider = ({ children }) => {
  const [userId] = useState("krish"); // ✅ added userId
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [sessions, setSessions] = useState([]);
  const [activeSession, setActiveSession] = useState(null);

  const addMessage = (msg) => {
    setMessages((prev) => [...prev, msg]);
  };

  const switchSession = (sessionId) => {
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
        userId, // ✅ exposed here
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