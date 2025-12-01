from database import SessionLocal, engine
from models import Base, User, Source

Base.metadata.create_all(bind=engine)

db = SessionLocal()

if not db.query(User).first():
    demo_user = User(username="demo", api_key="demo-key-CHANGE_ME")
    db.add(demo_user)

if not db.query(Source).first():
    sources_list = [
        Source(name="Source 1", description="Description 1"),
        Source(name="Source 2", description="Description 2")
    ]
    db.add_all(sources_list)

db.commit()
db.close()

print("Sample data created. Demo API key: demo-key-CHANGE_ME")
