from src.agents.llm_client import LLMClient

class ValidatorAgent:
    def __init__(self):
        self.llm = LLMClient()

    def run(self, query: str) -> str:
        prompt = (
            "Validate the following MongoDB query. "
            "Respond with either VALID or INVALID and a short reason.\n\n"
            f"Query: {query}"
        )
        return self.llm.chat(prompt)
