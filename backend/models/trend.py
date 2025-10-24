from sqlalchemy import Column, String, Float, DateTime, JSON, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from .database import Base
import uuid

class TrendAnalysis(Base):
    __tablename__ = "trend_analysis"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    style = Column(String(100), nullable=False)
    trend_score = Column(Float, default=0.0)
    seasonal_factor = Column(Float, default=1.0)
    region = Column(String(100))
    analysis_data = Column(JSON, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class LocalStore(Base):
    __tablename__ = "local_stores"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    address = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    phone = Column(String(20))
    website = Column(String)
    store_type = Column(String(50))  # gallery, furniture_store, art_supply
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class StoreInventory(Base):
    __tablename__ = "store_inventory"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    store_id = Column(UUID(as_uuid=True), nullable=False)
    artwork_id = Column(UUID(as_uuid=True), nullable=False)
    available = Column(Boolean, default=True)
    stock_quantity = Column(Integer, default=0)
    last_updated = Column(DateTime(timezone=True), server_default=func.now())
