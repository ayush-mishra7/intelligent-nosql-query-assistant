from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.translator_agent import TranslatorAgent
from src.agents.validator_agent import ValidatorAgent
from src.agents.optimizer_agent import OptimizerAgent

app = FastAPI(title="Intelligent NoSQL Analyzer API", version="1.0.0")

translator = TranslatorAgent()
validator = ValidatorAgent()
optimizer = OptimizerAgent()

class QueryRequest(BaseModel):
    instruction: str

class QueryResponse(BaseModel):
    instruction: str
    query: str
    validation: str
    optimization: str

@app.post("/analyze", response_model=QueryResponse)
def analyze(req: QueryRequest):
    nl = req.instruction.strip()
    query = translator.run(nl)
    validation = validator.run(query)
    optimization = optimizer.run(query)
    return QueryResponse(
        instruction=nl,
        query=query,
        validation=validation,
        optimization=optimization
    )
