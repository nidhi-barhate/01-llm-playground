from fastapi import APIRouter

from schemas.chat_request import ChatRequest
from schemas.chat_response import ChatResponse
from services.llm_service import LLMService

router = APIRouter()

llm_service = LLMService()


@router.post("/chat")
def chat(request: ChatRequest) -> ChatResponse:
    response = llm_service.chat(request.prompt)
    return ChatResponse(output=response)