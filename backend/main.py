from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import uvicorn
import os
from dotenv import load_dotenv

# Import models and database
from models.database import get_db
from models.artwork import Artwork
from models.user import UserProfile, RoomUpload, Session as UserSession
from models.trend import TrendAnalysis, LocalStore

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Art.Decor.AI API",
    description="AI-powered interior design and decoration API with multimodal input support",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
@app.get("/")
async def root():
    return {
        "message": "Art.Decor.AI API is running",
        "version": "1.0.0",
        "features": [
            "Multimodal input (photo, text, voice)",
            "AI-powered décor recommendations",
            "Style analysis and matching",
            "Local store integration"
        ]
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": "2024-01-01T00:00:00Z"}

# Artwork endpoints
@app.get("/artworks")
async def get_artworks(
    skip: int = 0,
    limit: int = 20,
    style: str = None,
    price_min: float = None,
    price_max: float = None,
    db: Session = Depends(get_db)
):
    """Get artworks with optional filtering"""
    query = db.query(Artwork)
    
    if style:
        query = query.filter(Artwork.style_tags.contains([style]))
    
    if price_min is not None:
        query = query.filter(Artwork.price >= price_min)
    
    if price_max is not None:
        query = query.filter(Artwork.price <= price_max)
    
    artworks = query.offset(skip).limit(limit).all()
    return {
        "artworks": [
            {
                "id": str(artwork.id),
                "title": artwork.title,
                "brand": artwork.brand,
                "price": artwork.price,
                "style_tags": artwork.style_tags,
                "dominant_palette": artwork.dominant_palette,
                "image_url": artwork.image_url,
                "dimensions": artwork.dimensions,
                "description": artwork.description
            }
            for artwork in artworks
        ],
        "total": query.count(),
        "skip": skip,
        "limit": limit
    }

@app.get("/artworks/{artwork_id}")
async def get_artwork(artwork_id: str, db: Session = Depends(get_db)):
    """Get a specific artwork by ID"""
    artwork = db.query(Artwork).filter(Artwork.id == artwork_id).first()
    if not artwork:
        raise HTTPException(status_code=404, detail="Artwork not found")
    
    return {
        "id": str(artwork.id),
        "title": artwork.title,
        "brand": artwork.brand,
        "price": artwork.price,
        "style_tags": artwork.style_tags,
        "dominant_palette": artwork.dominant_palette,
        "image_url": artwork.image_url,
        "dimensions": artwork.dimensions,
        "description": artwork.description,
        "created_at": artwork.created_at.isoformat()
    }

# Style and trend endpoints
@app.get("/styles")
async def get_available_styles(db: Session = Depends(get_db)):
    """Get all available artwork styles"""
    # Get unique styles from artwork tags
    artworks = db.query(Artwork).all()
    all_tags = []
    for artwork in artworks:
        all_tags.extend(artwork.style_tags)
    
    unique_styles = list(set(all_tags))
    return {"styles": unique_styles}

@app.get("/trends")
async def get_trend_analysis(db: Session = Depends(get_db)):
    """Get current trend analysis"""
    trends = db.query(TrendAnalysis).all()
    return {
        "trends": [
            {
                "style": trend.style,
                "trend_score": trend.trend_score,
                "seasonal_factor": trend.seasonal_factor,
                "region": trend.region,
                "analysis_data": trend.analysis_data
            }
            for trend in trends
        ]
    }

# User profile endpoints
@app.get("/users/{user_id}/profile")
async def get_user_profile(user_id: str, db: Session = Depends(get_db)):
    """Get user profile and preferences"""
    profile = db.query(UserProfile).filter(UserProfile.id == user_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="User profile not found")
    
    return {
        "id": str(profile.id),
        "preferred_styles": profile.preferred_styles,
        "color_profile": profile.color_profile,
        "budget_range": profile.budget_range,
        "created_at": profile.created_at.isoformat(),
        "updated_at": profile.updated_at.isoformat()
    }

# Room analysis endpoints (placeholder for Week 2)
@app.post("/rooms/analyze")
async def analyze_room():
    """Analyze uploaded room image - Week 2 implementation"""
    return {
        "message": "Room analysis endpoint - to be implemented in Week 2",
        "features": [
            "Wall detection using YOLOv8",
            "Color palette extraction",
            "Lighting analysis",
            "Style classification"
        ]
    }

# Recommendation endpoints (placeholder for Week 3-4)
@app.post("/recommendations")
async def get_recommendations():
    """Get AI-powered décor recommendations - Week 3-4 implementation"""
    return {
        "message": "Recommendation endpoint - to be implemented in Week 3-4",
        "features": [
            "Vision-Match Agent integration",
            "FAISS vector search",
            "Multimodal reasoning",
            "Personalized suggestions"
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
