from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Source, User
from auth import verify_api_key

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/sources")
def get_sources(api_key: str, db: Session = Depends(get_db)):
    user = verify_api_key(api_key, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid API key")

    sources = db.query(Source).all()
    return sources


@app.get("/")
def root():
    return {"message": "CTI API is running"}