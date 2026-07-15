import re


class ClauseSplitter:

    def __init__(self, text):

        self.text = text

    def split_clauses(self):

        clauses = re.split(r"(?=### \d+\.)", self.text)

        clauses = [x.strip() for x in clauses if x.strip()]

        return clauses
