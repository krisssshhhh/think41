import React from "react";
import { ChatProvider } from "./context/ChatContext";
import ChatWindow from "./components/ChatWindow";
import "./App.css";

function App() {
  return (
    <ChatProvider>
      <div className="App">
        <h2>🧠 AI Chatbot</h2>
        <ChatWindow />
      </div>
    </ChatProvider>
  );
}

export default App;