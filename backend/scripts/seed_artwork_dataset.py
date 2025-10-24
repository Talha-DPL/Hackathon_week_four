#!/usr/bin/env python3
"""
Artwork Dataset Seeding Script
Creates a curated dataset of 500+ artworks for Art.Decor.AI
"""

import json
import random
from datetime import datetime
from typing import List, Dict
import uuid
from sqlalchemy.orm import Session
from models.database import SessionLocal, engine
from models.artwork import Artwork, ArtworkEmbedding
from models.database import Base

# Create tables
Base.metadata.create_all(bind=engine)

# Artwork styles and their characteristics
ARTWORK_STYLES = {
    "abstract": {
        "tags": ["modern", "contemporary", "geometric", "colorful"],
        "palettes": [
            ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"],
            ["#FF9A9E", "#FECFEF", "#FECFEF", "#FAD0C4"],
            ["#A8E6CF", "#FFD3A5", "#FFAAA5", "#FF8B94"]
        ]
    },
    "minimalist": {
        "tags": ["clean", "simple", "monochrome", "geometric"],
        "palettes": [
            ["#FFFFFF", "#F5F5F5", "#E0E0E0", "#BDBDBD"],
            ["#2C3E50", "#34495E", "#7F8C8D", "#BDC3C7"],
            ["#F8F9FA", "#E9ECEF", "#DEE2E6", "#CED4DA"]
        ]
    },
    "vintage": {
        "tags": ["retro", "classic", "warm", "nostalgic"],
        "palettes": [
            ["#8B4513", "#D2691E", "#CD853F", "#F4A460"],
            ["#2F4F4F", "#708090", "#A9A9A9", "#D3D3D3"],
            ["#8B0000", "#B22222", "#DC143C", "#FF6347"]
        ]
    },
    "nature": {
        "tags": ["organic", "green", "natural", "botanical"],
        "palettes": [
            ["#228B22", "#32CD32", "#90EE90", "#98FB98"],
            ["#8FBC8F", "#9ACD32", "#ADFF2F", "#7FFF00"],
            ["#2E8B57", "#3CB371", "#20B2AA", "#40E0D0"]
        ]
    },
    "bohemian": {
        "tags": ["eclectic", "colorful", "patterned", "artistic"],
        "palettes": [
            ["#FF1493", "#FF69B4", "#FFB6C1", "#FFC0CB"],
            ["#8A2BE2", "#9370DB", "#BA55D3", "#DA70D6"],
            ["#FF4500", "#FF6347", "#FF7F50", "#FFA500"]
        ]
    },
    "industrial": {
        "tags": ["urban", "metallic", "raw", "modern"],
        "palettes": [
            ["#2F4F4F", "#708090", "#A9A9A9", "#D3D3D3"],
            ["#696969", "#808080", "#A9A9A9", "#C0C0C0"],
            ["#8B0000", "#B22222", "#DC143C", "#FF6347"]
        ]
    }
}

# Price ranges by style
PRICE_RANGES = {
    "abstract": (50, 500),
    "minimalist": (30, 300),
    "vintage": (40, 400),
    "nature": (35, 350),
    "bohemian": (60, 600),
    "industrial": (45, 450)
}

# Brands by style
BRANDS = {
    "abstract": ["Modern Art Co.", "Contemporary Canvas", "Abstract Expressions"],
    "minimalist": ["Clean Lines", "Simple Spaces", "Minimal Design Co."],
    "vintage": ["Retro Revival", "Classic Collection", "Vintage Vibes"],
    "nature": ["Natural Elements", "Botanical Art", "Green Living"],
    "bohemian": ["Boho Chic", "Eclectic Arts", "Free Spirit"],
    "industrial": ["Urban Edge", "Industrial Design", "Metro Art"]
}

def generate_artwork_data(style: str, count: int) -> List[Dict]:
    """Generate artwork data for a specific style"""
    artworks = []
    style_data = ARTWORK_STYLES[style]
    
    for i in range(count):
        palette = random.choice(style_data["palettes"])
        price_range = PRICE_RANGES[style]
        brand = random.choice(BRANDS[style])
        
        artwork = {
            "title": f"{style.title()} {random.choice(['Composition', 'Study', 'Expression', 'Piece', 'Work'])} #{i+1}",
            "brand": brand,
            "price": round(random.uniform(price_range[0], price_range[1]), 2),
            "style_tags": style_data["tags"] + [style],
            "dominant_palette": {
                "colors": palette,
                "primary": palette[0],
                "secondary": palette[1] if len(palette) > 1 else palette[0],
                "accent": palette[2] if len(palette) > 2 else palette[0]
            },
            "image_url": f"https://example-artwork-images.com/{style}/{i+1}.jpg",
            "dimensions": {
                "width": random.choice([24, 30, 36, 48, 60]),
                "height": random.choice([24, 30, 36, 48, 60]),
                "unit": "inches"
            },
            "description": f"A beautiful {style} artwork featuring {', '.join(palette[:2])} tones. Perfect for {random.choice(['living rooms', 'bedrooms', 'offices', 'dining areas'])}."
        }
        artworks.append(artwork)
    
    return artworks

def seed_artwork_dataset():
    """Seed the database with artwork data"""
    db = SessionLocal()
    
    try:
        # Clear existing data
        db.query(ArtworkEmbedding).delete()
        db.query(Artwork).delete()
        db.commit()
        
        all_artworks = []
        
        # Generate artworks for each style
        for style in ARTWORK_STYLES.keys():
            count = random.randint(80, 120)  # 80-120 artworks per style
            style_artworks = generate_artwork_data(style, count)
            all_artworks.extend(style_artworks)
        
        # Shuffle to randomize order
        random.shuffle(all_artworks)
        
        # Insert artworks
        for artwork_data in all_artworks:
            artwork = Artwork(**artwork_data)
            db.add(artwork)
        
        db.commit()
        print(f"✅ Successfully seeded {len(all_artworks)} artworks")
        
        # Generate some sample embeddings (placeholder)
        artworks = db.query(Artwork).all()
        for artwork in artworks[:50]:  # Generate embeddings for first 50
            # Placeholder embedding (512 dimensions of random values)
            embedding_vector = [random.uniform(-1, 1) for _ in range(512)]
            
            embedding = ArtworkEmbedding(
                vector=embedding_vector,
                artwork_id=artwork.id
            )
            db.add(embedding)
        
        db.commit()
        print(f"✅ Generated embeddings for 50 artworks")
        
    except Exception as e:
        print(f"❌ Error seeding dataset: {e}")
        db.rollback()
    finally:
        db.close()

def create_sample_trend_data():
    """Create sample trend analysis data"""
    db = SessionLocal()
    
    try:
        from models.trend import TrendAnalysis
        
        trends = [
            {
                "style": "minimalist",
                "trend_score": 0.85,
                "seasonal_factor": 1.2,
                "region": "global",
                "analysis_data": {
                    "popularity": "high",
                    "season": "spring",
                    "demographics": ["millennials", "gen_z"]
                }
            },
            {
                "style": "nature",
                "trend_score": 0.78,
                "seasonal_factor": 1.5,
                "region": "global",
                "analysis_data": {
                    "popularity": "rising",
                    "season": "spring",
                    "demographics": ["all_ages"]
                }
            },
            {
                "style": "bohemian",
                "trend_score": 0.65,
                "seasonal_factor": 0.9,
                "region": "global",
                "analysis_data": {
                    "popularity": "stable",
                    "season": "all",
                    "demographics": ["young_adults"]
                }
            }
        ]
        
        for trend_data in trends:
            trend = TrendAnalysis(**trend_data)
            db.add(trend)
        
        db.commit()
        print("✅ Created trend analysis data")
        
    except Exception as e:
        print(f"❌ Error creating trend data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("🌱 Starting artwork dataset seeding...")
    seed_artwork_dataset()
    create_sample_trend_data()
    print("🎉 Dataset seeding completed!")
