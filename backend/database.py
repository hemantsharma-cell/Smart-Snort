from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
SQLALCHEMY_DATABASE_URL = "sqlite:///./snort_alerts.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# helper function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()