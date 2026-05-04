from aip.core.base_agent import AgentResult
from aip.core.model_router import ModelRouter


class Summarizer:
    """Aggregates outputs from multiple agents into a final response."""

    def __init__(self, model_router: ModelRouter):
        self.router = model_router

    def summarize(self, query: str, results: list[AgentResult]) -> str:
        combined = "\n\n".join(
            f"[{r.agent_name}]\n{r.output}" for r in results
        )
        messages = [
            {
                "role": "system",
                "content": "Synthesize the following agent outputs into a clear, concise answer.",
            },
            {
                "role": "user",
                "content": f"Original query: {query}\n\nAgent outputs:\n{combined}",
            },
        ]
        return self.router.chat(messages)
