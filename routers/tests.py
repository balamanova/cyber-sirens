from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException
import json
from db import get_db
from models import TestSubmission
from schemas import CognitiveTest, TestSubmissionCreate,TestResultResponse
from sqlalchemy.orm import Session
from test_interpreter import interpret_phq9, interpret_gad7, interpret_pss

test_router = APIRouter()

# Load cognitive tests from JSON
with open("routers/files/cognitive_tests.json", "r", encoding="utf-8") as f:
    cognitive_tests = json.load(f)

@test_router.get("/tests/", response_model=List[CognitiveTest])
def get_tests():
    return cognitive_tests  # Make sure this matches the model structure

@test_router.get("/tests/{name}", response_model=CognitiveTest)
async def get_test(name: str):
    test = next((test for test in cognitive_tests if test["name"] == name), None)
    if test is None:
        raise HTTPException(status_code=404, detail="Test not found")
    return test

@test_router.post("/tests/submit", response_model=TestResultResponse)
async def submit_test_result(submission: TestSubmissionCreate, db: Session = Depends(get_db)):
    new_submission = TestSubmission(
        test_id=submission.test_id,
        user_id=submission.user_id,
        score=submission.score,
        submitted_at=datetime.utcnow(),
    )

    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)

    try:
        result = handle_test_submission(submission)  # Handle the result interpretation
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return result


def handle_test_submission(submission: TestSubmissionCreate) -> TestResultResponse:
    if submission.test_id == "Depression":
        return interpret_phq9(submission.score)
    elif submission.test_id == "Anxiety":
        return interpret_gad7(submission.score)
    elif submission.test_id == "Stress":
        return interpret_pss(submission.score)
    else:
        raise ValueError("Unknown test type")
