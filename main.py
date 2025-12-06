from src.agents.translator_agent import TranslatorAgent
from src.agents.validator_agent import ValidatorAgent
from src.agents.optimizer_agent import OptimizerAgent

if __name__ == "__main__":
    text = input("Enter natural language instruction: ")

    translator = TranslatorAgent()
    validator = ValidatorAgent()
    optimizer = OptimizerAgent()

    query = translator.run(text)
    validation = validator.run(query)
    optimization = optimizer.run(query)

    print("\n=== MONGODB ANALYSIS ===\n")
    print("Generated Query:\n", query)
    print("\nValidation:\n", validation)
    print("\nOptimization Suggestions:\n", optimization)
