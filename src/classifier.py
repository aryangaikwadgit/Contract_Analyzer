import ollama

from src.config import Config
from src.prompts import PromptManager


class ClauseClassifier:

    def classify(

            self,

            clause,

            similar_clause):


        response = ollama.chat(

            model=Config.MODEL_NAME,

            messages=[

                {

                    "role": "system",

                    "content":

                    PromptManager.SYSTEM_PROMPT
                },

                {

                    "role": "user",

                    "content":

                    f"""

                    Contract Clause:

                    {clause}


                    Similar Risky Clause:

                    {similar_clause}

                    """
                }

            ]
        )

        return response[
            "message"
        ][
            "content"
        ]