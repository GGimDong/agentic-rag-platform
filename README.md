# Agentic RAG Platform

Multi-agent orchestration platform with RAG pipeline, designed as a reusable AI Service Layer.

## Architecture

![Architecture](Architect.png)

### Layers

**Application**
- Sends requests and receives answers from the AI Service Layer.

**AI Service Layer (Orchestration)**
- **Supervisor (Query Router)**: Classifies incoming requests and routes them to the appropriate Task Agent.
- **Task Agents (Domain Specific)**: Specialist agents that handle domain-specific tasks. The vehicle diagnosis scenario (Diagnostic Agent, Driving Assistant, Repair Advisor) is provided as an example implementation.
- **Summarizer**: Aggregates agent outputs into a final response.
- **RAG Retriever**: Retrieves relevant context from Vector DB to support agent reasoning.
- **Model Router**: Routes inference requests to either a local runtime or a cloud LLM API depending on configuration. Current implementation targets **local** (llama.cpp).

**AI Core Layer**
- **Vector DB**: Stores embedded documents for RAG retrieval (FAISS).
- **AI Runtime**: Local inference runtime (llama.cpp).
- **AI Model (LLM/VLM)**: Underlying models served by the runtime.

## Project Structure

```
agentic-rag-platform/
├── platform/                  # Generic orchestration layer (reusable)
│   ├── core/
│   │   ├── base_agent.py      # SpecialistAgent abstract base class
│   │   ├── supervisor.py      # Query routing logic
│   │   ├── rag_retriever.py   # RAG retrieval (domain-agnostic)
│   │   ├── model_router.py    # Local / Cloud inference routing
│   │   └── summarizer.py      # Response aggregation
│   └── pipeline/
│       └── graph.py           # LangGraph pipeline assembly
│
└── examples/
    └── vehicle_diagnosis/     # Domain-specific implementation example
        ├── agents/
        │   ├── diagnostic_agent.py
        │   ├── driving_assistant.py
        │   └── repair_advisor.py
        ├── data/
        └── app.py
```

## Stack
- **Orchestration**: LangGraph
- **LLM Runtime**: llama.cpp (local)
- **RAG**: FAISS + sentence-transformers
- **API**: FastAPI
