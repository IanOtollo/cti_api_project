import os
from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_api_key(authorization: str = Header(...), db: Session = Depends(get_db)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    
    token = authorization.replace("Bearer ", "")
    
    env_api_key = os.environ.get("DEMO_API_KEY")
    
    if token != env_api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    user = db.query(User).filter(User.api_key == token).first()
    return user
