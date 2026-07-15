from sentence_transformers import SentenceTransformer


class Embedder:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def encode(self, texts):

        embedding = self.model.encode(texts, convert_to_numpy=True)

        return embedding
