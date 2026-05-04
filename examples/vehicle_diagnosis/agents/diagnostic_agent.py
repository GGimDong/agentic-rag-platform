from aip.core.base_agent import BaseAgent, AgentResult
from aip.core.model_router import ModelRouter


class DiagnosticAgent(BaseAgent):
    name = "diagnostic_agent"
    description = "Diagnoses vehicle faults based on symptoms and warning indicators"

    def __init__(self, model_router: ModelRouter):
        self.router = model_router

    def run(self, query: str, context: str) -> AgentResult:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a vehicle fault diagnostic expert.\n"
                    f"Use the following reference context to answer:\n{context}"
                ),
            },
            {"role": "user", "content": query},
        ]
        output = self.router.chat(messages)
        return AgentResult(agent_name=self.name, output=output)
