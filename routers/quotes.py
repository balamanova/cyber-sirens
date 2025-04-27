from fastapi import APIRouter
from pydantic import BaseModel
from typing import List


class Quote(BaseModel):
    id: int
    date: str
    text: str


quotes = [
    {
        "id": 1,
        "date": "2025-04-12",
        "text": "Life is what happens to you while you're busy making other plans.",
    },
    {
        "id": 2,
        "date": "2025-04-11",
        "text": "Happiness is when what you think, what you say, and what you do are in harmony.",
    },
    {
        "id": 3,
        "date": "2025-04-10",
        "text": "You can't stop the waves, but you can learn to surf.",
    },
    {
        "id": 4,
        "date": "2025-04-09",
        "text": "Do not go where the path may lead, go instead where there is no path and leave a trail.",
    },
    {
        "id": 5,
        "date": "2025-04-08",
        "text": "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    },
    {
        "id": 6,
        "date": "2025-04-07",
        "text": "Believe you can and you're halfway there.",
    },
    {
        "id": 7,
        "date": "2025-04-06",
        "text": "In the middle of every difficulty lies opportunity.",
    },
    {
        "id": 8,
        "date": "2025-04-05",
        "text": "What we think, we become.",
    },
    {
        "id": 9,
        "date": "2025-04-04",
        "text": "The only way to do great work is to love what you do.",
    },
    {
        "id": 10,
        "date": "2025-04-03",
        "text": "Everything you can imagine is real.",
    }
]


quotes_router = APIRouter()

@quotes_router.get("/quotes", response_model=List[Quote])
async def get_quotes():
    return quotes
