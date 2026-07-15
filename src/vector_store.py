import json
import faiss
import numpy as np

from src.embedder import Embedder


class VectorStore:

    def __init__(self):

        self.embedder = Embedder()

        self.index = None

        self.documents = []

    def build_index(self, path):

        with open(path, "r") as file:
            self.documents = json.load(file)

        # return self.documents, type(self.documents), self.documents[0]

        clauses = [
            x["clause"] for x in self.documents
        ]  # return only list of context clauses

        embeddings = self.embedder.encode(clauses)  # encoding context clauses

        embeddings = np.array(embeddings, dtype=np.float32)  #

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)


