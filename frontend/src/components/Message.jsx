import React from "react";
import "./Message.css";

const Message = ({ sender, text }) => {
  return (
    <div className={`message ${sender === "user" ? "user" : "ai"}`}>
      <p>{text}</p>
    </div>
  );
};

export default Message;