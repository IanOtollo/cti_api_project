import os
from database import SessionLocal, engine
from models import Base, User, Source

Base.metadata.create_all(bind=engine)

db = SessionLocal()

demo_api_key = os.environ.get("DEMO_API_KEY", "demo-key-CHANGE_ME")

if not db.query(User).first():
    demo_user = User(username="demo", api_key=demo_api_key)
    db.add(demo_user)

if not db.query(Source).first():
    sources_list = [
        Source(name="Source 1", description="Description 1"),
        Source(name="Source 2", description="Description 2")
    ]
    db.add_all(sources_list)

db.commit()
db.close()

print(f"Sample data created. Demo API key: {demo_api_key}")
