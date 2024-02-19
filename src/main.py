from similarity.model import Similarity

model = Similarity()
score = model.calculateScore("il aime les chats", "il aime les chiens")
print(score)