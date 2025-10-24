"""
Simplified Art.Decor.AI API for testing
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

app = FastAPI(
    title="Art.Decor.AI API",
    description="AI-powered interior design and decoration API",
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

# Mock data for testing
MOCK_ARTWORKS = [
    {
        "id": "1",
        "title": "Minimalist Abstract #1",
        "brand": "Modern Art Co.",
        "price": 150.0,
        "style_tags": ["minimalist", "abstract", "modern"],
        "dominant_palette": {
            "colors": ["#FFFFFF", "#E0E0E0", "#BDBDBD"],
            "primary": "#FFFFFF",
            "secondary": "#E0E0E0"
        },
        "image_url": "https://example.com/artwork1.jpg",
        "dimensions": {"width": 24, "height": 24, "unit": "inches"},
        "description": "A beautiful minimalist abstract piece perfect for modern spaces."
    },
    {
        "id": "2", 
        "title": "Nature Inspired #2",
        "brand": "Natural Elements",
        "price": 200.0,
        "style_tags": ["nature", "green", "organic"],
        "dominant_palette": {
            "colors": ["#228B22", "#32CD32", "#90EE90"],
            "primary": "#228B22",
            "secondary": "#32CD32"
        },
        "image_url": "https://example.com/artwork2.jpg",
        "dimensions": {"width": 30, "height": 30, "unit": "inches"},
        "description": "Inspired by nature with calming green tones."
    },
    {
        "id": "3",
        "title": "Vintage Classic #3", 
        "brand": "Retro Revival",
        "price": 180.0,
        "style_tags": ["vintage", "classic", "warm"],
        "dominant_palette": {
            "colors": ["#8B4513", "#D2691E", "#CD853F"],
            "primary": "#8B4513",
            "secondary": "#D2691E"
        },
        "image_url": "https://example.com/artwork3.jpg",
        "dimensions": {"width": 36, "height": 36, "unit": "inches"},
        "description": "A classic vintage piece with warm, nostalgic tones."
    }
]

MOCK_STYLES = ["minimalist", "abstract", "modern", "nature", "green", "organic", "vintage", "classic", "warm"]

MOCK_TRENDS = [
    {
        "style": "minimalist",
        "trend_score": 0.85,
        "seasonal_factor": 1.2,
        "region": "global",
        "analysis_data": {"popularity": "high", "season": "spring"}
    },
    {
        "style": "nature",
        "trend_score": 0.78,
        "seasonal_factor": 1.5,
        "region": "global", 
        "analysis_data": {"popularity": "rising", "season": "spring"}
    }
]

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

@app.get("/artworks")
async def get_artworks(
    skip: int = 0,
    limit: int = 20,
    style: str = None,
    price_min: float = None,
    price_max: float = None
):
    """Get artworks with optional filtering"""
    artworks = MOCK_ARTWORKS.copy()
    
    # Apply filters
    if style:
        artworks = [art for art in artworks if style in art["style_tags"]]
    
    if price_min is not None:
        artworks = [art for art in artworks if art["price"] >= price_min]
        
    if price_max is not None:
        artworks = [art for art in artworks if art["price"] <= price_max]
    
    # Apply pagination
    total = len(artworks)
    artworks = artworks[skip:skip + limit]
    
    return {
        "artworks": artworks,
        "total": total,
        "skip": skip,
        "limit": limit
    }

@app.get("/artworks/{artwork_id}")
async def get_artwork(artwork_id: str):
    """Get a specific artwork by ID"""
    artwork = next((art for art in MOCK_ARTWORKS if art["id"] == artwork_id), None)
    if not artwork:
        raise HTTPException(status_code=404, detail="Artwork not found")
    
    return artwork

@app.get("/styles")
async def get_available_styles():
    """Get all available artwork styles"""
    return {"styles": MOCK_STYLES}

@app.get("/trends")
async def get_trend_analysis():
    """Get current trend analysis"""
    return {"trends": MOCK_TRENDS}

@app.post("/rooms/analyze")
async def analyze_room():
    """Analyze uploaded room image - placeholder for future implementation"""
    return {
        "message": "Room analysis endpoint - to be implemented",
        "features": [
            "Wall detection using YOLOv8",
            "Color palette extraction", 
            "Lighting analysis",
            "Style classification"
        ]
    }

@app.post("/recommendations")
async def get_recommendations():
    """Get AI-powered décor recommendations - placeholder for future implementation"""
    return {
        "message": "Recommendation endpoint - to be implemented",
        "features": [
            "Vision-Match Agent integration",
            "FAISS vector search",
            "Multimodal reasoning", 
            "Personalized suggestions"
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
