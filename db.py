from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://cyber_sirens_obea_user:kkt3iNhpYWXA7QlcTWBuDD2vZYjFqDBZ@dpg-cvp8q5odl3ps73fue970-a.oregon-postgres.render.com/cyber_sirens_obea"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()