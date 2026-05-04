from aip.core.base_agent import BaseAgent, AgentResult
from aip.core.model_router import ModelRouter


class RepairAdvisor(BaseAgent):
    name = "repair_advisor"
    description = "Advises on repair options, urgency, and whether a service visit is needed"

    def __init__(self, model_router: ModelRouter):
        self.router = model_router

    def run(self, query: str, context: str) -> AgentResult:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a vehicle repair advisor. Assess repair urgency and recommend next steps.\n"
                    f"Reference context:\n{context}"
                ),
            },
            {"role": "user", "content": query},
        ]
        output = self.router.chat(messages)
        return AgentResult(agent_name=self.name, output=output)
