from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from typing import Dict, List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import date, datetime, timedelta

from db import get_db
from models import MoodEntry
from schemas import MoodEntryResponse, MoodInfo

router = APIRouter()

moods: Dict[int, Dict[str, str]] = {
    1: {"name": "Love", "description": "A feeling of attachment, care, and warmth towards someone or something.", "image_url": "https://example.com/love.jpg"},
    2: {"name": "Joy", "description": "A feeling of satisfaction, happiness, and cheerfulness.", "image_url": "https://example.com/joy.jpg"},
    3: {"name": "Sadness", "description": "A feeling of sorrow, loss, or disappointment.", "image_url": "https://example.com/sadness.jpg"},
    4: {"name": "Indifference", "description": "A lack of interest or emotion towards something.", "image_url": "https://example.com/indifference.jpg"},
    5: {"name": "Fear", "description": "A feeling of anxiety, worry, or apprehension.", "image_url": "https://example.com/fear.jpg"},
    6: {"name": "Anger", "description": "A strong feeling of irritation or displeasure.", "image_url": "https://example.com/anger.jpg"},
}

class MoodData(BaseModel):
    user_id: int
    mood_id: int
    user_comment: Optional[str] = None


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
    new_entry = MoodEntry(
        user_id=data.user_id, 
        mood_id=data.mood_id, 
        user_comment=data.user_comment  # Add user_comment if provided
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@router.get("/mood/{user_id}", response_model=List[MoodEntryResponse])
async def get_user_mood_entries(
    user_id: int,
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db)
):
    today = date.today()

    # Default to today if no date range is provided
    start_date = start_date or today
    end_date = end_date or today

    # Get all moods in the date range
    entries = db.query(MoodEntry).filter(
        and_(
            MoodEntry.user_id == user_id,
            MoodEntry.timestamp >= datetime.combine(start_date, datetime.min.time()),
            MoodEntry.timestamp <= datetime.combine(end_date, datetime.max.time())
        )
    ).all()

    # Build a map for quick lookup
    mood_by_date = {entry.timestamp.date(): entry for entry in entries}

    # Prepare response for every day in range
    days = (end_date - start_date).days + 1
    response = []
    for i in range(days):
        current_date = start_date + timedelta(days=i)
        mood_entry = mood_by_date.get(current_date)
        mood_details = moods.get(mood_entry.mood_id) if mood_entry else None

        if mood_details:
            # Populate the response with the details from the dictionary
          
            response.append(MoodEntryResponse(
                datetime=mood_entry.timestamp,
                mood=MoodInfo(
                    name=mood_details['name'],
                    user_comment=mood_entry.user_comment,
                    description=mood_details['description'],
                    image_url=mood_details['image_url']
                )
            ))
        else:
            response.append(MoodEntryResponse(
                datetime=datetime.combine(current_date, datetime.min.time()),
                mood=None
            ))

    return response
