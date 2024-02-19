from fastapi import FastAPI
from pydantic import BaseModel
from .similarity.model import Similarity
import time


app = FastAPI()
model = Similarity()


class SimilarityCalcul(BaseModel):
    sentence1: str
    sentence2: str


@app.get("/")
async def root():
    return {"message": "Welcome to sentence Similarity Model"}


@app.post("/similarity")
async def test_similarity(sentences: SimilarityCalcul):
    start = time.time()
    sentence1 = sentences.sentence1
    sentence2 = sentences.sentence2
    score = model.calculateScore(sentence1, sentence2)
    compute_time = time.time() - start
    return {
        "msg": "we calculated score succesfully",
        "sentence1": sentence1,
        "sentence2": sentence2,
        "score": score,
        "compute_time": compute_time
    }

