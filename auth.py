from sqlalchemy.orm import Session
from models import User

def verify_api_key(api_key: str, db: Session):
    return db.query(User).filter(User.api_key == api_key).first()
