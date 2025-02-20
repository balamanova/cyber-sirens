from typing import Optional
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr, constr
from passlib.context import CryptContext
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import jwt
import datetime

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

# Database setup
SQLALCHEMY_DATABASE_URL = "postgresql://sirens:LgpKxjvl4XoigXKhCd21yorfKQdimJF3@dpg-curn51bqf0us73fmjjog-a.oregon-postgres.render.com/sirens"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    phone_number = Column(String, nullable=True)
    gender = Column(String, nullable=True)

Base.metadata.create_all(bind=engine)

# Schemas
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

# Utils
def create_jwt_token(user_id: int):
    payload = {"user_id": user_id, "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)

# FastAPI app
app = FastAPI()

@app.post("/register")
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    hashed_password = hash_password(request.password)
    user = User(email=request.email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"user_id": user.id, "message": "Registration successful"}

@app.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_jwt_token(user.id)
    return {"token": token, "message": "Login successful"}

@app.put("/edit")
def edit_user(request: EditUserRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    update_data = request.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)
    
    db.commit()
    return {"message": "User updated successfully"}
