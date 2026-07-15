from langchain_core.prompts import PromptTemplate

from src.config import client
from src.models import ClauseAnalysis
from src.prompts import RAG_PROMPT
import json
from src.config import tracker


class RagChain:

    def __init__(self):

        prompt = PromptTemplate(
            template=RAG_PROMPT, input_variables=["clause", "context"]
        )

        self.chain = prompt | client

    def analyze(self, clause, context):

        context = json.dumps(context, indent=2)     

        response = self.chain.invoke({"clause": clause, "context": context})

        tracker.add_usage(response) # token tracker

        clean_response = (
            response.content.replace("```json", "").replace("```", "").strip()
        )

        clause_analysis = ClauseAnalysis.model_validate_json(clean_response)
        return clause_analysis
