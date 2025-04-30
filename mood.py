from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()

emotions = [
    {"id": 1, "name": "Любовь", "description": "Чувство привязанности, заботы и теплоты к кому-то или чему-то.", "image_url": "https://example.com/love.jpg"},
    {"id": 2, "name": "Радость", "description": "Чувство удовлетворения, счастья и веселья.", "image_url": "https://example.com/joy.jpg"},
    {"id": 3, "name": "Печаль", "description": "Чувство грусти, утраты или разочарования.", "image_url": "https://example.com/sadness.jpg"},
    {"id": 4, "name": "Безразличие", "description": "Отсутствие интереса или эмоций по отношению к чему-то.", "image_url": "https://example.com/indifference.jpg"},
    {"id": 5, "name": "Страх", "description": "Чувство тревоги, беспокойства или опасения.", "image_url": "https://example.com/fear.jpg"},
    {"id": 6, "name": "Гнев", "description": "Сильное раздражение или недовольство.", "image_url": "https://example.com/anger.jpg"}
]

cognitive_tests = [
    {"id": 1, "phq_9": "phq_9", "description": "Test description 1"},
    {"id": 2, "gad_7": "gad_7", "description": "Test description 2"},
    {"id": 2, "pss": "pss", "description": "Test description 2"}
]

class EmotionData(BaseModel):
    date: str
    user_id: int
    emotion_id: int

class CognitiveTestResult(BaseModel):
    test_id: int
    user_id: int
    score: int


@app.get("/emotions/", response_model=List[dict])
async def get_emotions():
    return emotions


@app.post("/emotions/")
async def post_emotion(data: EmotionData):

    print(f"Saved emotion data: {data}")
    return {"message": "Success"}


@app.get("/tests", response_model=List[dict])
async def get_tests():
    return cognitive_tests


@app.get("/tests/{id}", response_model=dict)
async def get_test(id: int):
    test = next((test for test in cognitive_tests if test["id"] == id), None)
    if test is None:
        raise HTTPException(status_code=404, detail="Test not found")
    return test


@app.post("/submit")
async def submit_result(result: CognitiveTestResult):
    print(f"Saved test result: {result}")
    
    result_message = "less stress" if result.score < 50 else "high stress"
    return {"message": "Success", "result": result_message}


quotes = [
    {
        "id": 1,
        "date": "2025-04-12",
        "text": "Жизнь — это то, что с тобой происходит, пока ты строишь планы.",
        "article_url": "https://example.com/articles/life-plans"
    },
    {
        "id": 2,
        "date": "2025-04-11",
        "text": "Счастье — это когда то, что ты думаешь, говоришь и делаешь, находится в гармонии.",
        "article_url": "https://example.com/articles/harmony"
    },
    {
        "id": 3,
        "date": "2025-04-10",
        "text": "Ты не можешь остановить волны, но можешь научиться серфить.",
        "article_url": "https://example.com/articles/surfing-life"
    }
]

class Quote(BaseModel):
    id: int
    date: str
    text: str
    article_url: str

@app.get("/quotes", response_model=List[Quote])
async def get_quotes():
    return quotes
