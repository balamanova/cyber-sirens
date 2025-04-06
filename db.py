from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://cyber_sirens_jt1i_user:4SxHVerXBjoOGZzRAqt2ed3xGgitKLuV@dpg-cvfgf31opnds73ba6r50-a.oregon-postgres.render.com/cyber_sirens_jt1i"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()