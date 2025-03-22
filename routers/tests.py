from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException
import json

from db import get_db
from models import TestSubmission
from schemas import CognitiveTest, TestSubmissionCreate
from sqlalchemy.orm import Session

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

@test_router.post("/tests/submit")
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

    return {"message": "Test result submitted successfully", "submission_id": new_submission.id}