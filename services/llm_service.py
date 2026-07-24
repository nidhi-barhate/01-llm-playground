from client.ollama_client import OllamaClient
class LLMService:
    def __init__(self):
        self.ollama_client = OllamaClient()

    def chat(self, message: str) -> str:
        return self.ollama_client.chat(message)