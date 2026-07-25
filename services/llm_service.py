from email.mime import message

from client.ollama_client import OllamaClient
from repository.message_repository import MessageRepository
from models.chat_model import Message
from sqlalchemy.orm import Session
from schemas.chat_request import ChatRequest

class LLMService:
    def __init__(self, db: Session):
        self.ollama_client = OllamaClient()
        self.message_repository = MessageRepository(db)

    def chat(self, request: ChatRequest) -> str:
        if request.is_new_chat_session:
            #clear the message history for a new chat session
            self.message_repository.delete_all()
            # Save the message to the database
            message_model = Message(role="user", content=request.prompt)
            self.message_repository.save(message_model)
            output = self.ollama_client.chat(request. prompt)
            # Save the output to the database
            llm_model = Message(role="assistant", content=output)
            self.message_repository.save(llm_model)
            return output
        else:
            # Retrieve the message history for the current chat session
            messages = self.message_repository.find_all()
            # Add the new user message to the history
            message_model = Message(role="user", content=request.prompt)
            messages.append(message_model)
             # Save the message to the database
            self.message_repository.save(message_model)
            # Send the message history to the Ollama API
            output = self.ollama_client.chat_with_memory(messages)
            # Save the output to the database
            llm_model = Message(role="assistant", content=output)
            self.message_repository.save(llm_model)
            return output    
        