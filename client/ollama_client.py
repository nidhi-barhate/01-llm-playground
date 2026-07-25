import requests
from config.settings import Settings
from models.chat_model import Message

class OllamaClient:
    def chat(self, prompt: str) -> str:
        url = f"{Settings.OLLAMA_BASE_URL}/api/chat"
        payload = {
            "model": Settings.OLLAMA_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False
        }
        print("Request JSON:")
        print(payload)
        response = requests.post(
            url=url,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        print("Status Code:", response.status_code)
        print("Response JSON:")
        print(response.json())

        return response.json()["message"]["content"]

    def chat_with_memory(self, messages: list[Message]) -> str:
        url = f"{Settings.OLLAMA_BASE_URL}/api/chat"
        payload = {
            "model": Settings.OLLAMA_MODEL,
            "messages": [
                {"role": message.role, "content": message.content} for message in messages
            ],
            "stream": False
        }
        print("Request JSON:")
        print(payload)
        response = requests.post(
            url=url,
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        print("Status Code:", response.status_code)
        print("Response JSON:")
        print(response.json())
        return response.json()["message"]["content"]