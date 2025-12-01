from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Source(Base):
    __tablename__ = 'sources'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    url = Column(String)
    last_fetch = Column(DateTime)
    indicators = relationship('Indicator', back_populates='source')

class Indicator(Base):
    __tablename__ = 'indicators'
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    value = Column(String, index=True)
    first_seen = Column(DateTime)
    last_seen = Column(DateTime)
    source_id = Column(Integer, ForeignKey('sources.id'))
    threat_category = Column(String)
    severity_score = Column(Integer)
    tags = Column(String)
    raw_payload = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    source = relationship('Source', back_populates='indicators')

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    api_key_hash = Column(String)
    role = Column(String, default='admin')