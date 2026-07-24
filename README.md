# 01 - LLM Playground

A simple playground to learn Large Language Models (LLMs) using **Python**, **FastAPI**, and **Ollama**.

The purpose of this project is to understand how an LLM works by building everything from scratch without using AI frameworks.

## Tech Stack

- Python
- FastAPI
- Pydantic
- Ollama
- Qwen Model
- Requests

## Features

- REST API with FastAPI
- Swagger UI
- Ollama Integration
- Local LLM Support
- Clean Layered Architecture

## Project Structure

```text
01-llm-playground/
│
├── client/
├── config/
├── controllers/
├── schemas/
├── services/
├── app.py
└── requirements.txt
```

## Run Ollama

Start Ollama:

```bash
ollama serve
```

Pull a model (if not installed):

```bash
ollama pull qwen3:8b
```

## Run the Application

```bash
uvicorn app:app --reload
```

Open Swagger:

```
http://localhost:8000/docs
```

## API

**POST** `/api/chat`

Request

```json
{
  "message": "Hello"
}
```

Response

```json
{
  "response": "Hello! How can I help you today?"
}
```

## Learning Journey

Current progress:

- ✅ FastAPI Setup
- ✅ REST API
- ✅ Service Layer
- ✅ Ollama Integration
- ✅ Local LLM