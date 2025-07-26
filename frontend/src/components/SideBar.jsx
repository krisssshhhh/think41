// components/Sidebar.jsx
import React, { useContext } from "react";
import { ChatContext } from "../context/ChatContext";
import "./Sidebar.css";

const Sidebar = () => {
  const { sessions, switchSession, saveSession, activeSession } = useContext(ChatContext);

  return (
    <div className="sidebar">
      <button onClick={saveSession}>+ New Chat</button>
      <h4>Conversations</h4>
      <ul>
        {sessions.map((s) => (
          <li
            key={s.id}
            onClick={() => switchSession(s.id)}
            className={activeSession === s.id ? "active" : ""}
          >
            Chat #{s.id}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;