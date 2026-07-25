from fastapi import APIRouter,Depends

from schemas.chat_request import ChatRequest
from schemas.chat_response import ChatResponse
from services.llm_service import LLMService
from sqlalchemy.orm import Session
from config.dependencies import get_db
router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    service = LLMService(db)
    return service.chat(request)