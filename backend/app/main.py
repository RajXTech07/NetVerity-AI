import importlib
import os
from typing import Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.routes.wifi import router as wifi_router
from app.routes.recommendation import router as rec_router

app = FastAPI(title="NetVerity.Ai")

# --- 1. Configure Gemini API ---
# It will securely look for the key in Render's environment variables
genai: Any = importlib.import_module("google.generativeai")
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set")

genai.configure(api_key=api_key)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(wifi_router)
app.include_router(rec_router)

# --- 2. Create the Data Model for the Chat Input ---
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Welcome to NetVerity.AI"}

# --- 3. Add the AI Chat Route ---
@app.post("/chat")
async def chat_with_gemini(request: ChatRequest):
    try:
        # Using 1.5-flash as it is the fastest for real-time web chat
        model = genai.GenerativeModel('gemini-pro')
        chat = model.start_chat(history=[])
        
        # We wrap the user's message in a prompt to give the AI context
        prompt = f"You are an expert network analyst assistant for NetVerity AI. Keep your answers brief, helpful, and focused on networking, speed, and trust scores. The user says: {request.message}"
        
        response = chat.send_message(prompt)
        
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))