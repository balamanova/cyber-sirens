from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Dict, List
from sqlalchemy.orm import Session

from db import get_db
from models import MoodEntry
from schemas import MoodEntryResponse

test_router = APIRouter()
cognitive_tests = [
    {
        "name": "phq_9",
        "description": "The PHQ-9 is a multipurpose instrument for screening, diagnosing, monitoring and measuring the severity of person's depression",
        "questions": [
            {
                "text": "How often have you been bothered by little interest or pleasure in doing things?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            },
            {
                "text": "How often have you been feeling down, depressed, or hopeless?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            },
            {
                "text": "How often have you had trouble falling or staying asleep, or sleeping too much?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            },
            {
                "text": "How often have you been feeling tired or having little energy?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            },
            {
                "text": "How often have you had a poor appetite or overeating?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            },
            {
                "text": "How often have you felt bad about yourself—or that you are a failure or have let yourself or your family down?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            },
            {
                "text": "How often have you had trouble concentrating on things, such as reading the newspaper or watching television?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            },
            {
                "text": "How often have you been moving or speaking so slowly that other people could have noticed? Or the opposite—being so fidgety or restless that you have been moving around a lot more than usual?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            },
            {
                "text": "How often have you thought that you would be better off dead, or of hurting yourself in some way?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            }
        ]
    },
        {
        "name": "gad_7",
        "description": "This test is a seven-item instrument that is used to measure or assess the severity of generalized anxiety disorder (GAD)",
        "questions": [
            {
                "text": "How often have you been feeling nervous, anxious, or on edge?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            },
            {
                "text": "How often have you not been able to stop or control worrying?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            },
            {
                "text": "How often have you worried too much about different things?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            },
            {
                "text": "How often have you had trouble relaxing?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            },
            {
                "text": "How often have you been so restless that it is hard to sit still?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            },
            {
                "text": "How often have you become easily annoyed or irritable?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            },
            {
                "text": "How often have you felt afraid, as if something awful might happen?",
                "answers": [
                    {"text": "Not at all", "score": 0},
                    {"text": "Several days", "score": 1},
                    {"text": "More than half the days", "score": 2},
                    {"text": "Nearly every day", "score": 3}
                ]
            }
        ]
    },
        {
        "name": "pss",
        "description": "This test is a classic stress assessment instrument, that is used to understand how different situations affect person's feelings and person's perceived stress",
        "questions": [
            {
                "text": "In the last month, how often have you felt that you were unable to control the important things in your life?",
                "answers": [
                    {"text": "Never", "score": 0},
                    {"text": "Almost never", "score": 1},
                    {"text": "Sometimes", "score": 2},
                    {"text": "Fairly often", "score": 3},
                    {"text": "Very often", "score": 4}
                ]
            },
            {
                "text": "In the last month, how often have you felt nervous and stressed?",
                "answers": [
                    {"text": "Never", "score": 0},
                    {"text": "Almost never", "score": 1},
                    {"text": "Sometimes", "score": 2},
                    {"text": "Fairly often", "score": 3},
                    {"text": "Very often", "score": 4}
                ]
            },
            {
                "text": "In the last month, how often have you felt confident about your ability to handle your personal problems?",
                "answers": [
                    {"text": "Never", "score": 4},
                    {"text": "Almost never", "score": 3},
                    {"text": "Sometimes", "score": 2},
                    {"text": "Fairly often", "score": 1},
                    {"text": "Very often", "score": 0}
                ]
            },
            {
                "text": "In the last month, how often have you felt that things were going your way?",
                "answers": [
                    {"text": "Never", "score": 4},
                    {"text": "Almost never", "score": 3},
                    {"text": "Sometimes", "score": 2},
                    {"text": "Fairly often", "score": 1},
                    {"text": "Very often", "score": 0}
                ]
            },
            {
                "text": "In the last month, how often have you felt that you could not cope with all the things that you had to do?",
                "answers": [
                    {"text": "Never", "score": 0},
                    {"text": "Almost never", "score": 1},
                    {"text": "Sometimes", "score": 2},
                    {"text": "Fairly often", "score": 3},
                    {"text": "Very often", "score": 4}
                ]
            },
            {
                "text": "In the last month, how often have you been able to control irritations in your life?",
                "answers": [
                    {"text": "Never", "score": 4},
                    {"text": "Almost never", "score": 3},
                    {"text": "Sometimes", "score": 2},
                    {"text": "Fairly often", "score": 1},
                    {"text": "Very often", "score": 0}
                ]
            },
            {
                "text": "In the last month, how often have you felt that you were on top of things?",
                "answers": [
                    {"text": "Never", "score": 4},
                    {"text": "Almost never", "score": 3},
                    {"text": "Sometimes", "score": 2},
                    {"text": "Fairly often", "score": 1},
                    {"text": "Very often", "score": 0}
                     ]
            }
        ]
    }
]


class CognitiveTestResult(BaseModel):
     test_name: str
     user_id: int
     answers: List[int]
    

@test_router.get("/tests/", response_model=List[dict])
async def get_tests():
     return cognitive_tests


@test_router.get("/tests/{name}", response_model=dict)
async def get_test(name: str):
     test = next((test for test in cognitive_tests if test["name"] == name), None)
     if test is None:
         raise HTTPException(status_code=404, detail="Test not found")
     return test

@test_router.post("/tests/result/", response_model=str)
async def calculate_result(test_result: CognitiveTestResult):
    test = next((test for test in cognitive_tests if test["name"] == test_result.test_name), None)
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")

total_score = sum(test["questions"][i]["answers"][answer]["score"] for i, answer in enumerate(test_result.answers))

result_message = ""
if test["name"] == "phq_9":
        if total_score <= 4:
            result_message = "Minimal depression"
        elif total_score <= 9:
            result_message = "Mild depression"
        elif total_score <= 14:
            result_message = "Moderate depression"
        elif total_score <= 19:
            result_message = "Moderately severe depression"
        else:
            result_message = "Severe depression"
elif test["name"] == "gad_7":

        if total_score <= 4:
            result_message = "Minimal anxiety"
        elif total_score <= 9:
            result_message = "Mild anxiety"
        elif total_score <= 14:
            result_message = "Moderate anxiety"
        else:
            result_message = "Severe anxiety"
elif test["name"] == "pss":

        if total_score <= 13:
            result_message = "Low stress"
        elif total_score <= 26:
            result_message = "Moderate stress"
        else:
            result_message = "High stress"

return result_message