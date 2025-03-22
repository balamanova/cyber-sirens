from pydantic import BaseModel, EmailStr, constr
from typing import Optional, List
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

class Answer(BaseModel):
    text: str
    score: int

class Question(BaseModel):
    text: str
    answers: List[Answer]

class CognitiveTest(BaseModel):
    name: str
    description: str
    questions: List[Question]
    
class TestSubmissionCreate(BaseModel):
    test_id: str
    user_id: int
    score: int
