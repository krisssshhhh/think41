# main.py
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from datetime import datetime
import psycopg2
import uuid

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Welcome to the E-commerce Chat API. Use POST /api/chat"}
# DB Connection
conn = psycopg2.connect(
    dbname="ecommerce_db",
    user="krishkumar",
    password="12345",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Request Body Schema
class ChatRequest(BaseModel):
    user_id: str
    message: str
    conversation_id: int | None = None

@app.post("/api/chat")
def chat_endpoint(chat: ChatRequest):
    # 1. Start a new conversation if none exists
    if chat.conversation_id is None:
        cursor.execute("INSERT INTO conversations (user_id) VALUES (%s) RETURNING id", (chat.user_id,))
        new_convo_id = cursor.fetchone()[0]
    else:
        new_convo_id = chat.conversation_id

    # 2. Store user message
    cursor.execute("""
        INSERT INTO messages (conversation_id, sender, message)
        VALUES (%s, %s, %s)
    """, (new_convo_id, 'user', chat.message))

    # 3. Placeholder AI response (LLM will come in Milestone 5)
    ai_response = f"You said: {chat.message}"

    # 4. Store AI message
    cursor.execute("""
        INSERT INTO messages (conversation_id, sender, message)
        VALUES (%s, %s, %s)
    """, (new_convo_id, 'ai', ai_response))

    conn.commit()

    return {
        "conversation_id": new_convo_id,
        "user_message": chat.message,
        "ai_response": ai_response
    }