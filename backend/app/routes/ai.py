from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_assistant import ask_ai

router = APIRouter()

class AIRequest(BaseModel):
    question: str
    wifi_data: dict


@router.post("/ask-ai")
def ask_ai_route(req: AIRequest):
    answer = ask_ai(req.question, req.wifi_data)
    return {"answer": answer}