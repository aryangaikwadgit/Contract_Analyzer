import json

import faiss

import numpy as np

from src.embeddings import Embedder


class VectorStore:

    def __init__(self):

        self.embedder = Embedder()

        self.index = None

        self.clauses = []

    def load_data(self):

        with open("data/risky_clauses.json", "r") as file:

            data = json.load(file)

        self.clauses = data

        vectors = []

        for item in data:

            vector = self.embedder.encode(item["clause"])

            vectors.append(vector)

        vectors = np.array(vectors)

        dimension = vectors.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(vectors)

    def search(self, query):

        query_vector = self.embedder.encode(query)

        query_vector = np.array([query_vector])

        distances, indices = self.index.search(query_vector, 1)

        return self.clauses[indices[0][0]]
