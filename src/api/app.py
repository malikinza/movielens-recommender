# src/api/app.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MovieLens MVP API")

class RecRequest(BaseModel):
    user_id: int
    n: int = 10

@app.get("/")
def read_root():
    return {"status": "ok", "service": "movielens-mvp"}

@app.post("/recommend")
def recommend(req: RecRequest):
    # Placeholder MVP: return empty list
    return {"user_id": req.user_id, "recommendations": []}
