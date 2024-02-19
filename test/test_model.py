import pytest
from src.similarity import model


class TestPrediction:

    def test_prediction(self):
        sentence1 = "il aime les chats"
        sentence2 = "il aime les chiens"
        modelPrediction = model.Similarity()  
        score = modelPrediction.calculateScore(sentence1, sentence2)  
        assert isinstance(score, float)




