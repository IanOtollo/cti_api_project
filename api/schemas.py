from pydantic import BaseModel
from typing import Optional, List, Any
from datetime import datetime

class IndicatorCreate(BaseModel):
    type: str
    value: str
    first_seen: Optional[datetime] = None
    last_seen: Optional[datetime] = None
    source: Optional[str] = None
    threat_category: Optional[str] = None
    severity_score: Optional[int] = None
    tags: Optional[List[str]] = None
    raw_payload: Optional[Any] = None
