from langchain_core.prompts import PromptTemplate

from src.config import client
from src.models import ContractClauses
from src.prompts import EXTRACT_PROMPT
from src.config import tracker

# class ClauseExtractor:

#     def __init__(self):

#         prompt = PromptTemplate(template=EXTRACT_PROMPT, input_variables=["contract"])

#         self.chain = prompt | client

#     def extract(self, contract):

#         response = self.chain.invoke({"contract": contract})

#         clean_response = (
#             response.content.replace("```json", "").replace("```", "").strip()
#         )

#         clauses = ContractClauses.model_validate_json(clean_response)

#         return clauses
    


class ClauseExtractor:
    def __init__(self):

        prompt = PromptTemplate(template=EXTRACT_PROMPT,input_variables=["contract"])

        self.chain = prompt | client

    def extract(self,contract):

        response = self.chain.invoke({"contract":contract})

        tracker.add_usage(response) # token tracker

        clean_response = response.content
        clean_response = (clean_response.replace("```json", "").replace("```", "").strip())

        # print(clean_response)
        clauses = ContractClauses.model_validate_json(clean_response)

        return clauses

