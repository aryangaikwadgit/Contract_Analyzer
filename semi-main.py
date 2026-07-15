from src.pdf_parser import PDFParser
from src.clause_extractor import ClauseExtractor
from src.retriever import Retriever
from src.rag_chain import RagChain
from src.report_generator import ReportGenerator
from src.models import ClauseResult
from src.memory import Memory
from src.question_answer import QAChain
from src.config import tracker


path = r"C:\Users\ARYAN\Downloads\doc2.pdf"


class Test:

    def __init__(self):

        self.path = path
        self.text = None

        self.obj_parser = PDFParser()
        self.obj_clause_extract = ClauseExtractor()
        self.retriever = Retriever()
        self.obj_rag_chain = RagChain()
        self.obj_report = ReportGenerator()

    def run(self):

        self.text = self.obj_parser.extract_text(self.path)

        self.contract = self.obj_clause_extract.extract(self.text)

        clause_results = []
        
        for clause in self.contract.clauses:

            context = self.retriever.ret(clause.clause)

            rag_out = self.obj_rag_chain.analyze(
                clause.clause,
                context,
            )

            clause_results.append(
                ClauseResult(
                    title=clause.title,
                    clause=clause.clause,
                    analysis=rag_out,
                )
            )

        final_report = self.obj_report.generate(clause_results)

        return final_report


if __name__ == "__main__":

    contract_ai = Test()

    final_report = contract_ai.run()

    report = final_report.model_dump_json(indent=2)
    print(report)

    

    memory = Memory()

    qa = QAChain()

    while True:

        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        history = memory.load()

        answer = qa.ask(
            report=report,
            history=history,
            question=question,
        )

        print("\nAnswer:\n")

        print(answer)

        memory.save(question, answer)

    # tracker.print_summary()