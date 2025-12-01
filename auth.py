from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User

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
    user = db.query(User).filter(User.api_key == token).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    return user
