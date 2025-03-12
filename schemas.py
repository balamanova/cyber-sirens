from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import datetime

class RegisterRequest(BaseModel):
    email: EmailStr
    password: constr(min_length=6)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class EditUserRequest(BaseModel):
    user_id: int
    name: Optional[str] = None
    age: Optional[int] = None
    phone_number: Optional[str] = None
    gender: Optional[str] = None

class MoodEntryResponse(BaseModel):
    id: int
    user_id: int
    mood_id: int 
    timestamp: datetime 
    