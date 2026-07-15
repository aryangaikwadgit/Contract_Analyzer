from langchain_classic.memory import ConversationBufferMemory


class Memory:

    def __init__(self):

        self.memory = ConversationBufferMemory(
            return_messages=True
        )

    def save(self, question, answer):

        self.memory.save_context(
            {"input": question},
            {"output": answer}
        )   

    def load(self):

        return self.memory.load_memory_variables({})

    def clear(self):

        self.memory.clear()

        