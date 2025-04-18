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
    }
]


quotes_router = APIRouter()

@quotes_router.get("/quotes", response_model=List[Quote])
async def get_quotes():
    return quotes
