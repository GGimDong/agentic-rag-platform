from aip.core.base_agent import BaseAgent
from aip.core.model_router import ModelRouter


class Supervisor:
    """Routes incoming queries to the appropriate specialist agents."""

    def __init__(self, agents: list[BaseAgent], model_router: ModelRouter):
        self.agents = {a.name: a for a in agents}
        self.router = model_router

    def route(self, query: str) -> list[str]:
        agent_descriptions = "\n".join(
            f"- {name}: {agent.description}"
            for name, agent in self.agents.items()
        )
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a query router. Select the most relevant agents for the query.\n"
                    f"Available agents:\n{agent_descriptions}\n\n"
                    "Respond with agent names only, separated by commas. No explanation."
                ),
            },
            {"role": "user", "content": query},
        ]
        response = self.router.chat(messages)
        selected = [name.strip() for name in response.split(",")]
        return [name for name in selected if name in self.agents]
