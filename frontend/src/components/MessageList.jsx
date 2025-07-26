import React, { useContext } from "react";
import { ChatContext } from "../context/ChatContext";
import Message from "./Message";

const MessageList = () => {
  const { messages } = useContext(ChatContext);

  return (
    <div className="message-list">
      {messages.map((msg, idx) => (
        <Message key={idx} sender={msg.sender} text={msg.text} />
      ))}
    </div>
  );
};

export default MessageList;