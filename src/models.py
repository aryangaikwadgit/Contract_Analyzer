from pydantic import BaseModel


class Clause(BaseModel):

    title: str
    clause: str


class ContractClauses(BaseModel):

    clauses: list[Clause]


class ClauseAnalysis(BaseModel):
    meaning: str
    risk_score: int
    classification: str
    reason: str
    explanation: str
    concerns: str           # always a string now
    negotiation_tip: str    # always a string now


# class ClauseAnalysisList(BaseModel):

#     analyses: list[ClauseAnalysis]


# class ClauseBatch(BaseModel):

#     title: str
#     clause: str
#     context: list[dict]


class ClauseResult(BaseModel):

    title: str
    clause: str
    analysis: ClauseAnalysis


class ContractReport(BaseModel):

    risk_score: int
    risk_level: str
    summary: str
    negotiation_points: list[str]
    clauses: list[ClauseResult]