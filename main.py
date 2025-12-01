from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Source, User
from auth import verify_api_key, get_db

app = FastAPI()

@app.get("/sources")
def get_sources(current_user: User = Depends(verify_api_key), db: Session = Depends(get_db)):
    sources = db.query(Source).all()
    return sources

@app.get("/")
def root():
    return {"message": "CTI API is running"}
