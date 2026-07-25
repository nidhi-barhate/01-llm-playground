from pydantic import BaseModel

class ChatRequest(BaseModel):
    is_new_chat_session: bool
    prompt:str