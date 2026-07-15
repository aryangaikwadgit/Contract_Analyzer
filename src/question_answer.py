from langchain_core.prompts import ChatPromptTemplate

from src.config import client
from src.prompts import QUESTION_PROMPT
from src.config import tracker



class QAChain:

    def __init__(self):

        prompt = ChatPromptTemplate.from_template(QUESTION_PROMPT)

        self.chain = prompt | client

    def ask(self, report, history, question):

        response = self.chain.invoke(
            {
                "report": report,
                "history": history,
                "question": question,
            }
        )

        tracker.add_usage(response) # token tracker


        return response.content
