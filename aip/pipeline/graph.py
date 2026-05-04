from typing import TypedDict
from langgraph.graph import StateGraph, END

from aip.core.base_agent import BaseAgent, AgentResult
from aip.core.supervisor import Supervisor
from aip.core.rag_retriever import RAGRetriever
from aip.core.summarizer import Summarizer


class PipelineState(TypedDict):
    query: str
    selected_agents: list[str]
    retrieved_docs: list[str]
    agent_outputs: list[AgentResult]
    final_answer: str


def build_pipeline(
    supervisor: Supervisor,
    rag_retriever: RAGRetriever,
    agents: dict[str, BaseAgent],
    summarizer: Summarizer,
):
    def supervisor_node(state: PipelineState) -> dict:
        selected = supervisor.route(state["query"])
        return {"selected_agents": selected}

    def rag_node(state: PipelineState) -> dict:
        docs = rag_retriever.retrieve(state["query"])
        return {"retrieved_docs": docs}

    def agents_node(state: PipelineState) -> dict:
        context = "\n\n".join(state["retrieved_docs"])
        results = [
            agents[name].run(state["query"], context)
            for name in state["selected_agents"]
            if name in agents
        ]
        return {"agent_outputs": results}

    def summarizer_node(state: PipelineState) -> dict:
        answer = summarizer.summarize(state["query"], state["agent_outputs"])
        return {"final_answer": answer}

    graph = StateGraph(PipelineState)
    graph.add_node("supervisor", supervisor_node)
    graph.add_node("rag", rag_node)
    graph.add_node("agents", agents_node)
    graph.add_node("summarizer", summarizer_node)

    graph.set_entry_point("supervisor")
    graph.add_edge("supervisor", "rag")
    graph.add_edge("rag", "agents")
    graph.add_edge("agents", "summarizer")
    graph.add_edge("summarizer", END)

    return graph.compile()
