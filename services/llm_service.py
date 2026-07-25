from email.mime import message

from client.ollama_client import OllamaClient
from repository.message_repository import MessageRepository
from models.chat_model import Message
from sqlalchemy.orm import Session

class LLMService:
    def __init__(self, db: Session):
        self.ollama_client = OllamaClient()
        self.message_repository = MessageRepository(db)

    def chat(self, prompt: str) -> str:
        # Save the message to the database
        llm_model = Message(role="user", content=prompt)
        self.message_repository.save(llm_model)
        output = self.ollama_client.chat(prompt)
        # Save the output to the database
        llm_model = Message(role="assistant", content=output)
        self.message_repository.save(llm_model)
        return output