from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llm_utils import ask_llm
from db_utils import get_top_5_products, get_order_status, get_stock_for_product
import re

app = FastAPI()

# ✅ CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "✅ Backend is live!"}

# ✅ Pydantic Model
class ChatRequest(BaseModel):
    user_id: str
    message: str

# ✅ Chat Endpoint
@app.post("/api/chat")
def chat(req: ChatRequest):
    try:
        msg = req.message.lower()

        # 🎯 Intent 1: Top 5 Sold Products
        if "top" in msg and "product" in msg and "sold" in msg:
            top_products = get_top_5_products()
            product_list = "\n".join([
                f"{i+1}. {name} ({sold} sold)"
                for i, (name, sold) in enumerate(top_products)
            ])
            prompt = f"""
You are a helpful assistant. Format the following product sales summary into a clean, numbered list for the user:

{product_list}

Ensure the list is short, clear, and structured.
"""
            ai_reply = ask_llm(prompt)

        # 🎯 Intent 2: Order Status
        elif "order id" in msg or "status of order" in msg:
            match = re.search(r"order\s+id\s+(\d+)", msg)
            if match:
                order_id = match.group(1)
                result = get_order_status(order_id)
                if result:
                    status, shipped_at, delivered_at, returned_at = result
                    info = f"Order {order_id} status: {status}. Shipped: {shipped_at}, Delivered: {delivered_at}, Returned: {returned_at}."
                    prompt = f"Customer asked about order status. Here's the info: {info}. Write a clear response."
                    ai_reply = ask_llm(prompt)
                else:
                    ai_reply = f"❌ No order found with ID {order_id}."
            else:
                ai_reply = "⚠️ Please provide a valid order ID like: 12345."

        # 🎯 Intent 3: Stock Check
        elif "how many" in msg and "in stock" in msg:
            match = re.search(r"how many (.+?) (are )?in stock", msg)
            if match:
                product = match.group(1).strip()
                stock_count = get_stock_for_product(product)
                prompt = f"""
There are {stock_count} units of '{product}' in stock.

Write a helpful and friendly message for the user including the product name and stock quantity.
"""
                ai_reply = ask_llm(prompt)
            else:
                ai_reply = "⚠️ Please specify a product name, like 'Classic T-Shirts'."

        # 🧠 Fallback to LLM for general questions
        else:
            ai_reply = ask_llm(req.message)

        return {
            "user_id": req.user_id,
            "user_message": req.message,
            "ai_response": ai_reply
        }

    except Exception as e:
        return {
            "error": str(e),
            "hint": "Check your API key, DB connection, or request format."
        }