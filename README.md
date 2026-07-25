# 🤖 01 - LLM Playground

A conversational AI backend built from scratch using **Python**, **FastAPI**, **SQLite**, and **Ollama**.

This project demonstrates the core architecture behind modern LLM-powered applications by implementing conversation memory, persistent chat history, and local Large Language Model (LLM) integration without relying on AI frameworks such as LangChain or LlamaIndex.

---

## 🎯 Objectives

- Build a conversational AI backend from scratch
- Understand how LLM APIs communicate using structured messages
- Implement persistent conversation memory
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
- Local LLM Integration (Ollama)
- Persistent Conversation Memory
- Multi-turn Context-Aware Conversations
- SQLAlchemy ORM
- Repository Pattern
- Service Layer Architecture
- Clean Layered Design

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

Download the model (if not already installed)

```bash
ollama pull qwen3:8b
```

### Run the Application

```bash
uvicorn app:app --reload
```

Open Swagger UI

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
| `new_chat` | Boolean | `true` starts a new conversation by clearing the existing conversation history. `false` continues the current conversation by loading the previous messages and sending them to the LLM as context. |
| `prompt` | String | User's input message. |

### Response

```json
{
  "response": "Hello! How can I help you today?"
}
```

---

## 🧠 Conversation Memory

This project demonstrates how conversational memory works in LLM applications.

### New Conversation

```json
{
  "new_chat": true,
  "prompt": "Hello"
}
```

Flow

```text
Clear Conversation History
        │
        ▼
Save User Message
        │
        ▼
Send Current Prompt to LLM
        │
        ▼
Save Assistant Response
```

---

### Continue Conversation

```json
{
  "new_chat": false,
  "prompt": "What is my name?"
}
```

Flow

```text
Load Conversation History
        │
        ▼
Append Current User Message
        │
        ▼
Convert Messages to LLM Payload
        │
        ▼
Send Complete Conversation
        │
        ▼
Receive Assistant Response
        │
        ▼
Save Assistant Response
```

This enables the model to generate context-aware responses by using the complete conversation history instead of only the latest prompt.

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
Convert Database Records → LLM Messages
      │
      ▼
Send Request to Ollama
      │
      ▼
Receive Assistant Response
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
- Prompt Construction
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
- How to integrate local LLMs with Ollama
- How to design a clean, maintainable backend architecture
- How SQLAlchemy and SQLite manage conversation data
- How context-aware AI applications reconstruct conversation history before sending requests to an LLM

This project was intentionally built without AI orchestration frameworks to gain a deeper understanding of the fundamental building blocks behind modern AI applications.