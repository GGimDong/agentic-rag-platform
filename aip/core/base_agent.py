from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class AgentResult:
    agent_name: str
    output: str


class BaseAgent(ABC):
    name: str
    description: str

    @abstractmethod
    def run(self, query: str, context: str) -> AgentResult:
        ...
