from src.pdf_parser import PDFParser
from src.clause_extractor import ClauseExtractor
from src.retriever import Retriever
from src.rag_chain import RagChain
from src.report_generator import ReportGenerator
from src.models import ClauseResult


class ContractAI:

    def __init__(self):

        self.obj_parser = PDFParser()
        self.obj_clause_extract = ClauseExtractor()
        self.retriever = Retriever()
        self.obj_rag_chain = RagChain()
        self.obj_report = ReportGenerator()

    def analyze(self, pdf_path):

        text = self.obj_parser.extract_text(pdf_path)

        contract = self.obj_clause_extract.extract(text)

        clause_results = []

        for clause in contract.clauses:

            context = self.retriever.ret(clause.clause)

            analysis = self.obj_rag_chain.analyze(
                clause.clause,
                context,
            )

            clause_results.append(
                ClauseResult(
                    title=clause.title,
                    clause=clause.clause,
                    analysis=analysis,
                )
            )

        final_report = self.obj_report.generate(
            clause_results
        )

        return final_report