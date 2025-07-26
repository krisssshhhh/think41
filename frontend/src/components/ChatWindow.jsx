// components/ChatWindow.jsx
import React, { useContext } from "react";
import Sidebar from "./SideBar";
import MessageList from "./MessageList";
import UserInput from "./UserInput";
import "./ChatWindow.css";
import { ChatContext } from "../context/ChatContext";

const ChatWindow = () => {
  const { messages } = useContext(ChatContext);

  return (
    <div className="chat-container">
      <Sidebar />
      <div className="chat-window">
        <MessageList messages={messages} />
        <UserInput />
      </div>
    </div>
  );
};

export default ChatWindow;