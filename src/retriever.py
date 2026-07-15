import numpy as np

from src.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.vector_store = VectorStore()

        self.vector_store.build_index("data/knowledge_base.json")

    def ret(self,query,k=3):
        qe = self.vector_store.embedder.encode([query])
        qe = np.array(qe, dtype=np.float32)
        distances, indices = self.vector_store.index.search(qe,k)
        results = []
        for index in indices[0]:
            result = self.vector_store.documents[index]
            results.append(result)

        return results



        # print(qe.shape())
        # print(distances)
        # print(indices)


#     def retrieve(self, query, k=3):

#         query_embedding = self.vector_store.embedder.encode([query])

#         query_embedding = np.array(query_embedding, dtype=np.float32)

#         distances, indices = self.vector_store.index.search(query_embedding, k)

#         context = ""

#         for index in indices[0]:

#             document = self.vector_store.documents[index]

#             context += f"""
# Clause:
# {document["clause"]}

# Risk:
# {document["risk"]}

# Reason:
# {document["reason"]}

# Suggestion:
# {document["suggestion"]}

# -------------------------

# """

#         return context
