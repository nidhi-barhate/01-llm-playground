# 🤖 01 - LLM Playground

A conversational AI backend built from scratch using **Python**, **FastAPI**, **SQLite**, and **Ollama**.

This project focuses on understanding the core architecture behind modern LLM applications without relying on AI frameworks such as LangChain or LlamaIndex.

It demonstrates how conversation memory, message history, and local LLM integration work under the hood.

---

## 🎯 Project Goals

- Build a conversational AI backend from scratch
- Understand the LLM request/response lifecycle
- Implement conversation memory
- Learn clean layered architecture
- Integrate a locally hosted Large Language Model

---

## 🚀 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | SQLite |
| LLM | Ollama + Qwen 3 |
| Validation | Pydantic |
| HTTP Client | Requests |

---

## ✨ Key Features

- ✅ RESTful Chat API
- ✅ Interactive Swagger Documentation
- ✅ Local LLM Integration (Ollama)
- ✅ Multi-turn Conversation Memory
- ✅ Persistent Chat History
- ✅ SQLAlchemy ORM
- ✅ Repository Pattern
- ✅ Service Layer Architecture
- ✅ Clean Modular Design

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

## ⚙️ Getting Started

### Start Ollama

```bash
ollama serve
```

Download the model (if required)

```bash
ollama pull qwen3:8b
```

### Run the Application

```bash
uvicorn app:app --reload
```

Open Swagger UI

```
http://localhost:8000/docs
```

---

## 📡 REST API

### POST `/api/chat`

### Request

```json
{
  "message": "Hello"
}
```

### Response

```json
{
  "response": "Hello! How can I help you today?"
}
```

---

## 💬 Conversation Memory

Unlike a simple prompt-response application, this project stores every conversation in SQLite.

Each request follows this flow:

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
Convert History to LLM Messages
      │
      ▼
Call Ollama
      │
      ▼
Receive Assistant Response
      │
      ▼
Save Assistant Message
      │
      ▼
Return Response
```

This enables the model to maintain conversational context across multiple interactions.

---

## 🧠 Concepts Explored

- LLM API Integration
- Chat Message Roles (`system`, `user`, `assistant`)
- Conversation Memory
- Prompt Construction
- Local Model Execution
- SQLAlchemy ORM
- Repository Pattern
- Layered Architecture
- FastAPI REST APIs
- SQLite Persistence

---

## 🎓 Learning Outcome

This project helped me understand the internal architecture of conversational AI systems by implementing:

- LLM communication using REST APIs
- Persistent conversation history
- Context-aware multi-turn conversations
- Clean backend architecture following software engineering best practices

Instead of relying on AI frameworks, every component was built from first principles to gain a deeper understanding of how modern LLM applications work.

---

## 📍 Project Status

**✅ Completed**

This project is the first milestone in my AI Engineering learning journey and serves as the foundation for upcoming projects on Prompt Engineering, Function Calling, RAG, AI Agents, and Enterprise AI Systems.