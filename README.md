# agentic-rag-platform

Multi-agent orchestration platform with RAG pipeline.

Built as a reference implementation of an AI Service Layer — covering Supervisor routing, RAG retrieval, specialized Agents, and response summarization.

## Architecture

```
Application
    ↕
AI Service Layer
  ├── Supervisor        # Query routing & orchestration
  ├── RAG Retriever     # Vector DB retrieval
  ├── Agent Pool
  │   ├── Fault Diagnosis Agent
  │   ├── Repair Advisor Agent
  │   ├── Driver Assistant Agent
  │   └── Image Select Agent (VLM)
  └── Summarizer        # Response aggregation
        ↕
AI Core Layer
  ├── LLM (llama.cpp)
  ├── VLM (Qwen2.5-VL)
  └── Vector DB (FAISS)
```

## Stack
- **Orchestration**: LangGraph
- **LLM Runtime**: llama.cpp
- **RAG**: FAISS + sentence-transformers
- **VLM**: Qwen2.5-VL
- **API**: FastAPI