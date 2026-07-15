from src.models import ClauseResult

class Scorer:

    WEIGHTS = {
        "Fair": 0.5,
        "Moderate": 1.0,
        "Risky": 1.5,
    }

    def score_calculate(self, clause_list):

        if not clause_list:
            return 0, "Low"

        weighted_sum = 0
        total_weight = 0

        for clause in clause_list:

            risk_score = clause.analysis.risk_score
            classification = clause.analysis.classification

            weight = self.WEIGHTS.get(classification, 1.0)

            weighted_sum += risk_score * weight
            total_weight += weight

        overall_score = round(weighted_sum / total_weight)

        if overall_score <= 25:
            overall_risk = "Low"

        elif overall_score <= 50:
            overall_risk = "Medium"

        else:
            overall_risk = "High"

        return overall_score, overall_risk






# class Scorer:
    
#     def score_calculate(self, clause_list):
        
#         total = len(clause_list)

#         risky = 0

#         for clause in clause_list:

#             if clause.analysis.classification == "Risky":

#                 risky += 1

#         if total == 0:

#             return 100, "Low"

#         score = int(((total - risky) / total) * 100)

#         if score >= 80:

#             level = "Low"

#         elif score >= 60:

#             level = "Medium"

#         else:

#             level = "High"

#         return score, level







# from src.models import ClauseResult


# class Score:
#     def score_calculate(self, clause_list):
        
#         total_clause = len(clause_list)

#         risky = 0

#         for clause in clause_list:
#             if clause.analysis.classification ==  "Risky":
#                 risky = risky + 1

#         if total_clause == 0:
#             return 0, "low"
        
#         score = int((risky/total_clause)*100)

#         if score <= 20:
#             level = "low"

#         elif score <= 40:
#             level = "medium"

#         else:
#             level = "high"

#         return  score, level

