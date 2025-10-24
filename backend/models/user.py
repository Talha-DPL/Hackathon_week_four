from sqlalchemy import Column, String, DateTime, JSON, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from .database import Base
import uuid

class UserProfile(Base):
    __tablename__ = "user_profiles"
    
    id = Column(UUID(as_uuid=True), primary_key=True)
    preferred_styles = Column(ARRAY(String), default=[])
    color_profile = Column(JSON, default={})
    budget_range = Column(JSON, default={"min": 0, "max": 1000})
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class RoomUpload(Base):
    __tablename__ = "room_upload"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    room_type = Column(String(50))
    s3_url = Column(String, nullable=False)
    palette_json = Column(JSON, default={})
    lighting_json = Column(JSON, default={})
    wall_detection_json = Column(JSON, default={})
    style_analysis = Column(JSON, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Session(Base):
    __tablename__ = "session"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    query_text = Column(String)
    query_type = Column(String(20))  # photo, text, voice
    topk_ids = Column(ARRAY(UUID), default=[])
    chosen_id = Column(UUID(as_uuid=True))
    rationale = Column(String)
    satisfaction_score = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
