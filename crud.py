from sqlalchemy.orm import Session
from models import Indicator, Source, User
from typing import Optional

def create_source_if_not_exists(db: Session, name: str):
    src = db.query(Source).filter(Source.name == name).first()
    if src:
        return src
    src = Source(name=name)
    db.add(src)
    db.commit()
    db.refresh(src)
    return src

def create_indicator(db: Session, ind, source_name: Optional[str] = None):
    src = create_source_if_not_exists(db, source_name) if source_name else None
    tags_str = ','.join(ind.tags) if getattr(ind, "tags", None) else None
    indicator = Indicator(
        type=ind.type,
        value=ind.value,
        first_seen=ind.first_seen,
        last_seen=ind.last_seen,
        source_id=src.id if src else None,
        threat_category=ind.threat_category,
        severity_score=ind.severity_score,
        tags=tags_str,
        raw_payload=ind.raw_payload
    )
    db.add(indicator)
    db.commit()
    db.refresh(indicator)
    return indicator

def get_user_by_api_key_hash(db: Session, api_key_hash: str):
    return db.query(User).filter(User.api_key_hash == api_key_hash).first()
