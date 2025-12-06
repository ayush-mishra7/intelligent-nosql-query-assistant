from src.agents.llm_client import LLMClient

class OptimizerAgent:
    def __init__(self):
        self.llm = LLMClient()

    def run(self, query: str) -> str:
        prompt = (
            "Suggest performance improvements for this MongoDB query. "
            "Include possible index recommendations.\n\n"
            f"Query: {query}"
        )
        return self.llm.chat(prompt)
