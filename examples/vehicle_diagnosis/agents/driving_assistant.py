from aip.core.base_agent import BaseAgent, AgentResult
from aip.core.model_router import ModelRouter


class DrivingAssistant(BaseAgent):
    name = "driving_assistant"
    description = "Provides safe driving guidance and immediate actions for the driver"

    def __init__(self, model_router: ModelRouter):
        self.router = model_router

    def run(self, query: str, context: str) -> AgentResult:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a driving safety assistant. Provide clear, immediate actions the driver should take.\n"
                    f"Reference context:\n{context}"
                ),
            },
            {"role": "user", "content": query},
        ]
        output = self.router.chat(messages)
        return AgentResult(agent_name=self.name, output=output)
