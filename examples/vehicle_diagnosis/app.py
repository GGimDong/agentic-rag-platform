from aip.core.model_router import ModelRouter, Backend
from aip.core.rag_retriever import RAGRetriever
from aip.core.supervisor import Supervisor
from aip.core.summarizer import Summarizer
from aip.pipeline.graph import build_pipeline

from examples.vehicle_diagnosis.agents.diagnostic_agent import DiagnosticAgent
from examples.vehicle_diagnosis.agents.driving_assistant import DrivingAssistant
from examples.vehicle_diagnosis.agents.repair_advisor import RepairAdvisor


def create_pipeline():
    router = ModelRouter(backend=Backend.LOCAL)
    rag = RAGRetriever()

    # TODO: load actual vehicle manual documents
    rag.build(["Placeholder document. Replace with actual vehicle manual content."])

    agents = [
        DiagnosticAgent(router),
        DrivingAssistant(router),
        RepairAdvisor(router),
    ]

    supervisor = Supervisor(agents, router)
    summarizer = Summarizer(router)

    return build_pipeline(
        supervisor=supervisor,
        rag_retriever=rag,
        agents={a.name: a for a in agents},
        summarizer=summarizer,
    )


if __name__ == "__main__":
    pipeline = create_pipeline()
    result = pipeline.invoke({
        "query": "엔진 경고등이 켜졌어요. 어떻게 해야 하나요?",
        "selected_agents": [],
        "retrieved_docs": [],
        "agent_outputs": [],
        "final_answer": "",
    })
    print(result["final_answer"])
