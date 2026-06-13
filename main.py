from src.vector_store import VectorStore
from src.classifier import ClauseClassifier


store = VectorStore()

store.load_data()

classifier = ClauseClassifier()


clause = """

Employer owns all intellectual property created outside work hours.

"""


similar_clause = store.search(
    clause
)


result = classifier.classify(
    clause,
    similar_clause
)

print(result)