from pydantic import BaseModel

class ChatRequest(BaseModel):
    new_chat: bool
    prompt:str