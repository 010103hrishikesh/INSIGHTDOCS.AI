from fastapi import FastAPI
from pydantic import BaseModel

from rag_pipeline import ask_question
from ingest import ingest

app = FastAPI()


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "RAG API Running"}


@app.post("/upload")
def upload():

    ingest("data/uploaded.pdf")

    return {
        "message": "PDF processed successfully"
    }


@app.post("/ask")
def ask(query: QueryRequest):

    answer = ask_question(query.question)

    return {
        "answer": answer
    }