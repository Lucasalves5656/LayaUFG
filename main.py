from fastapi import FastAPI
from pydantic import BaseModel
import laya

app = FastAPI(title="Laya API")

# Inicializa o modelo
agent = laya.load()

class DecisionRequest(BaseModel):
    state: str
    questions: list[dict]

@app.get("/")
def health_check():
    return {"status": "online", "model": "laya-0.4b"}

@app.post("/decide")
def decide(req: DecisionRequest):
    result = agent.decide(state=req.state, questions=req.questions)
    return result