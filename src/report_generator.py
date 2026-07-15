from src.models import ContractReport
from src.scorer import Scorer


class ReportGenerator:

    def generate(self, clause_results):

        scorer = Scorer()

        overall_score, overall_risk = scorer.score_calculate(clause_results)

        fair = 0
        moderate = 0
        risky = 0

        requires_attention = []

        for clause in clause_results:

            classification = clause.analysis.classification

            if classification == "Fair":
                fair += 1

            elif classification == "Moderate":
                moderate += 1
                requires_attention.append(clause.title)

            else:
                risky += 1
                requires_attention.append(clause.title)

        total = len(clause_results)

        if overall_risk == "Low":

            summary = (
                f"This contract contains {total} analysed clauses. "
                "Overall, the agreement appears balanced and follows standard employment practices. "
                "No significant legal concerns were identified, though you should always review the terms carefully before signing."
            )

        elif overall_risk == "Medium":

            summary = (
                f"This contract contains {total} analysed clauses. "
                "Overall, the agreement presents a moderate level of risk. "
                "Some clauses deserve careful review to ensure they align with your expectations and protect your interests."
            )

        else:

            summary = (
                f"This contract contains {total} analysed clauses. "
                "Overall, the agreement presents a high level of risk. "
                "Several provisions may significantly affect your rights and obligations as an employee. "
                "Review the highlighted clauses carefully and consider seeking clarification or negotiating these terms before signing."
            )

        report = ContractReport(
            risk_score=overall_score,
            risk_level=overall_risk,
            summary=summary,
            negotiation_points=requires_attention,  # rename this in your model later
            clauses=clause_results,
        )

        return report


# from src.models import (
#     ClauseResult,
#     ContractReport,
# )

# from src.scorer import Scorer


# class ReportGenerator:

#     def generate(self, clause_results):

#         scorer = Scorer()

#         score, level = scorer.score_calculate(clause_results)

#         negotiation_points = []

#         for clause in clause_results:

#             if clause.analysis.classification == "Risky":

#                 negotiation_points.append(clause.title)

#         if len(negotiation_points) == 0:

#             summary = "The contract appears fair with no major concerns."

#         else:

#             summary = (
#                 f"The contract contains {len(negotiation_points)} risky clause(s). "
#                 "Review them carefully before signing."
#             )

#         report = ContractReport(
#             risk_score=score,
#             risk_level=level,
#             summary=summary,
#             negotiation_points=negotiation_points,
#             clauses=clause_results,
#         )

#         return report
