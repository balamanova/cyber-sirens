from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Dict, List
from sqlalchemy.orm import Session

from db import get_db
from models import MoodEntry
from schemas import MoodEntryResponse

router = APIRouter()

moods: Dict[int, Dict[str, str]] = {
    1: {"name": "Любовь", "description": "Чувство привязанности, заботы и теплоты к кому-то или чему-то.", "image_url": "https://example.com/love.jpg"},
    2: {"name": "Радость", "description": "Чувство удовлетворения, счастья и веселья.", "image_url": "https://example.com/joy.jpg"},
    3: {"name": "Печаль", "description": "Чувство грусти, утраты или разочарования.", "image_url": "https://example.com/sadness.jpg"},
    4: {"name": "Безразличие", "description": "Отсутствие интереса или эмоций по отношению к чему-то.", "image_url": "https://example.com/indifference.jpg"},
    5: {"name": "Страх", "description": "Чувство тревоги, беспокойства или опасения.", "image_url": "https://example.com/fear.jpg"},
    6: {"name": "Гнев", "description": "Сильное раздражение или недовольство.", "image_url": "https://example.com/anger.jpg"},
}

class MoodData(BaseModel):
    user_id: int
    mood_id: int


class Mood(BaseModel):
    id: int
    name: str
    description: str
    image_url: str

@router.get("/mood/", response_model=List[Mood])
async def get_moods():
    return [{"id": eid, **data} for eid, data in moods.items()]

# Post mood data with mapping
@router.post("/mood/")
async def save_mood(data: MoodData,  db: Session = Depends(get_db)):
    new_entry = MoodEntry(user_id=data.user_id, mood_id=data.mood_id)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@router.get("/mood/{user_id}", response_model=List[MoodEntryResponse])
async def get_user_mood_entries(user_id: int, db: Session = Depends(get_db)):
    mood_entries = db.query(MoodEntry).filter(MoodEntry.user_id == user_id).all()
    return mood_entries
