# 🤖 01 - LLM Playground

A conversational AI backend built from scratch using **Python**, **FastAPI**, **SQLite**, and **Ollama**.

This project demonstrates the core architecture behind modern LLM-powered applications by implementing conversation memory, persistent chat history, and real-time streaming responses without relying on AI orchestration frameworks such as LangChain or LlamaIndex.

---

## 🎯 Objectives

- Build a conversational AI backend from scratch
- Understand how LLM APIs communicate using structured messages
- Implement persistent conversation memory
- Stream AI responses in real time
- Learn clean layered backend architecture
- Integrate a locally hosted LLM using Ollama

---

## 🚀 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | FastAPI |
| Validation | Pydantic |
| ORM | SQLAlchemy |
| Database | SQLite |
| LLM | Ollama + Qwen 3 |
| HTTP Client | Requests |

---

## ✨ Features

- RESTful Chat API
- Interactive Swagger UI
- Local LLM Integration
- Persistent Conversation Memory
- Multi-turn Context-Aware Conversations
- Real-time Streaming Responses
- SQLAlchemy ORM
- Repository Pattern
- Service Layer Architecture
- Layered Architecture

---

## 🏛️ Architecture

```text
                 Client
                    │
                    ▼
         FastAPI REST Controller
                    │
                    ▼
              LLM Service
              /         \
             ▼           ▼
 Conversation Repository  Ollama Client
             │
             ▼
          SQLite
```

---

## 📂 Project Structure

```text
01-llm-playground
│
├── clients/
├── config/
├── controllers/
├── models/
├── repository/
├── schemas/
├── services/
├── app.py
└── requirements.txt
```

---

## ▶️ Getting Started

### Start Ollama

```bash
ollama serve
```

Pull the model

```bash
ollama pull qwen3:8b
```

Run the application

```bash
uvicorn app:app --reload
```

Open Swagger

```text
http://localhost:8000/docs
```

---

## 📡 REST API

### POST `/api/chat`

Starts a new conversation or continues an existing conversation.

### Request

```json
{
  "new_chat": true,
  "prompt": "Hello"
}
```

### Request Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `new_chat` | Boolean | Starts a new conversation when `true`; otherwise continues the existing conversation using stored history. |
| `prompt` | String | User input message. |

### Response

```json
{
  "response": "Hello! How can I help you today?"
}
```

---

## 🧠 Conversation Memory

When `new_chat` is `true`, the application clears the previous conversation and starts a fresh session.

When `new_chat` is `false`, it loads the previous messages from SQLite, reconstructs the conversation, appends the latest user prompt, and sends the complete context to the LLM.

This enables context-aware conversations across multiple user interactions.

---

## ⚡ Streaming Responses

The application also supports streaming responses from the LLM.

Instead of waiting for the complete response, the client receives small chunks of generated text as they become available.

### Non-Streaming

```text
User
   │
(wait)
   ▼
Complete Response
```

### Streaming

```text
User
   │
H
He
Hel
Hell
Hello
Hello!
...
```

Streaming provides a more responsive user experience and mirrors how modern AI chat applications display generated text.

---

## 💬 Conversation Flow

```text
User Prompt
      │
      ▼
Save User Message
      │
      ▼
Load Conversation History
      │
      ▼
Build LLM Message Payload
      │
      ▼
Send Request to Ollama
      │
      ▼
Receive Response (Streaming or Complete)
      │
      ▼
Save Assistant Response
      │
      ▼
Return Response
```

---

## 🧠 Concepts Explored

- LLM API Integration
- Chat Message Roles (`system`, `user`, `assistant`)
- Conversation Memory
- Context Reconstruction
- Streaming Responses
- Local Model Execution
- SQLAlchemy ORM
- Repository Pattern
- Service Layer
- Layered Architecture
- REST API Development with FastAPI

---

## 💡 Key Learnings

Building this project helped me understand:

- How conversational LLM applications communicate using structured messages
- The purpose of `system`, `user`, and `assistant` roles
- How conversation memory is implemented using persistent chat history
- How streaming responses improve user experience
- How to integrate local LLMs with Ollama
- How to design a clean and maintainable backend architecture
- How SQLAlchemy and SQLite manage conversation data
- How context-aware AI applications reconstruct conversation history before sending requests to an LLM

This project was intentionally built without AI orchestration frameworks to gain a deeper understanding of the fundamental building blocks behind modern AI applications.