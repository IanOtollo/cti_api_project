from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Source, User
from auth import verify_api_key

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "CTI API is running on Vercel"}

@app.get("/sources")
def get_sources(db: Session = Depends(get_db), current_user: User = Depends(verify_api_key)):
    return db.query(Source).all()
