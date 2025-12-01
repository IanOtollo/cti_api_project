from database import engine, Base, SessionLocal
from models import User
import hashlib


Base.metadata.create_all(bind=engine)


db = SessionLocal()
api_key = "demo-key-CHANGE_ME"
api_hash = hashlib.sha256(api_key.encode()).hexdigest()
if not db.query(User).filter(User.username=="demo").first():
    user = User(username="demo", api_key_hash=api_hash)
    db.add(user)
    db.commit()
    
db.close()
print("Demo API key:", api_key)