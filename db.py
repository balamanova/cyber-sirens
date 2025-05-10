from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://cyber_sirens_149d_user:pjp35K4HLrUjGurMQFkdPj0YU6Yc5smm@dpg-d0fkk1c9c44c73begr2g-a.oregon-postgres.render.com/cyber_sirens_149d"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()