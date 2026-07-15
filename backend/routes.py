import os
import tempfile

from fastapi import APIRouter, File, HTTPException, UploadFile

from backend.schemas import ChatRequest

from src.contract_ai_pipeline import ContractAI
from src.memory import Memory
from src.question_answer import QAChain


router = APIRouter()

contract_ai = ContractAI()

memory = Memory()
qa = QAChain()

final_report = None


@router.post("/analyze")
async def analyze_contract(file: UploadFile = File(...)):

    global final_report

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed.",
        )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:

        temp_file.write(await file.read())

        temp_path = temp_file.name

    try:

        final_report = contract_ai.analyze(temp_path)

        # New contract -> clear previous chat history
        memory.clear()

        return final_report

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)


@router.get("/report")
def get_report():

    global final_report

    if final_report is None:

        raise HTTPException(
            status_code=404,
            detail="No report found. Analyze a contract first.",
        )

    return final_report


@router.post("/chat")
def chat(request: ChatRequest):

    global final_report

    if final_report is None:

        raise HTTPException(
            status_code=400,
            detail="Analyze a contract first.",
        )

    report = final_report.model_dump_json(indent=2)

    history = memory.load()

    answer = qa.ask(
        report=report,
        history=history,
        question=request.question,
    )

    memory.save(
        request.question,
        answer,
    )

    return {
        "answer": answer
    }