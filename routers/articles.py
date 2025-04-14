from fastapi import APIRouter
from pydantic import BaseModel
from typing import List


class Article(BaseModel):
    quote_id: int
    url: str


articles = [
    {"quote_id": 1, "url": "https://example.com/articles/life-plans"},
    {"quote_id": 2, "url": "https://example.com/articles/harmony"},
    {"quote_id": 3, "url": "https://example.com/articles/surfing-life"}
]


articles_router = APIRouter()

@articles_router.get("/articles", response_model=List[Article])
async def get_articles():
    return articles
