from sqlalchemy import Column, String, Integer, Float, Text, DateTime, JSON, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from .database import Base
import uuid

class Artwork(Base):
    __tablename__ = "artwork"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    brand = Column(String(100))
    price = Column(Float)
    style_tags = Column(ARRAY(String), default=[])
    dominant_palette = Column(JSON, default={})
    image_url = Column(Text, nullable=False)
    dimensions = Column(JSON, default={})
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class ArtworkEmbedding(Base):
    __tablename__ = "artwork_embedding"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vector = Column(JSON)  # Will store the embedding vector
    artwork_id = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
