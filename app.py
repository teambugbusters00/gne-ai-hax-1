"""Prompt evaluation API. Run: pip install fastapi uvicorn; uvicorn app:app --reload"""
from fastapi import FastAPI
from pydantic import BaseModel,Field
app=FastAPI(title="GenAI Hackathon Copilot")
class Eval(BaseModel):prompt:str=Field(min_length=5);response:str=Field(min_length=1);criteria:list[str]=Field(default_factory=lambda:["correctness","clarity","specificity"])
@app.post("/evaluate")
def evaluate(x:Eval):
 text=(x.prompt+" "+x.response).lower(); scores={}
 for c in x.criteria:
  terms=[w for w in c.lower().split() if len(w)>3]; scores[c]=round(sum(t in text for t in terms)/max(1,len(terms)),2)
 return {"scores":scores,"coverage":round(sum(scores.values())/max(1,len(scores)),2),"note":"Heuristic baseline only; use human review or a validated judge model for real evaluation."}
@app.get("/")
def home():return {"project":"GenAI Hackathon Copilot","endpoint":"POST /evaluate"}