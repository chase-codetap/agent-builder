# OpenAI provider adapter stub
from .base import BaseProvider

class OpenAIProvider(BaseProvider):
    def run(self, prompt, model, **kwargs):
        # Implement OpenAI API call here
        return {"text": "stub", "tool_calls": [], "citations": []}
