from enum import Enum
from openai import OpenAI


class Backend(str, Enum):
    LOCAL = "local"
    CLOUD = "cloud"


class ModelRouter:
    """Routes inference requests to local (llama.cpp) or cloud LLM backend."""

    def __init__(
        self,
        backend: Backend = Backend.LOCAL,
        local_base_url: str = "http://localhost:8080",
        local_model: str = "local-model",
        cloud_model: str = "gpt-4o-mini",
    ):
        self.backend = backend
        self.local_model = local_model
        self.cloud_model = cloud_model

        if backend == Backend.LOCAL:
            self.client = OpenAI(base_url=f"{local_base_url}/v1", api_key="not-needed")
        else:
            self.client = OpenAI()  # uses OPENAI_API_KEY env var

    def chat(self, messages: list[dict], **kwargs) -> str:
        model = self.local_model if self.backend == Backend.LOCAL else self.cloud_model
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            **kwargs,
        )
        return response.choices[0].message.content
