from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.agent import ask_agent


router = APIRouter()


class AskRequest(BaseModel):
    question: str
    employee_id: str | None = None


@router.post("/ask")
def ask_assistant(request: AskRequest):
    answer = ask_agent(
        request.question,
        request.employee_id
    )

    return {
        "answer": answer
    }