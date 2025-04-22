from sqlalchemy.orm import Session
from models import Test, Question, Answer
from db import SessionLocal

cognitive_tests = [
    {
        "name": "Depression",
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
        "name": "Anxiety",
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
        "name": "Stress",
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

def create_cognitive_tests(db: Session):
    for test_data in cognitive_tests:
        test = Test(name=test_data['name'], description=test_data['description'])
        db.add(test)
        db.flush()

        for question_data in test_data['questions']:
            question = Question(test_id=test.id, text=question_data['text'])
            db.add(question)
            db.flush()

            for answer_data in question_data['answers']:
                answer = Answer(question_id=question.id, **answer_data)
                db.add(answer)

    db.commit()

if __name__ == "__main__":
    with SessionLocal() as db:
        create_cognitive_tests(db)


