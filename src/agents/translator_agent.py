from src.agents.llm_client import LLMClient

class TranslatorAgent:
    def __init__(self):
        self.llm = LLMClient()

    def run(self, text: str) -> str:
        prompt = (
            "Convert the following natural language instruction into a valid MongoDB query.\n"
            "Only return the query, no explanation.\n\n"
            f"Instruction: {text}"
        )
        return self.llm.chat(prompt)
