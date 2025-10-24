"""
Test database connection and basic operations
"""
import pytest
from sqlalchemy.orm import Session
from models.database import SessionLocal, engine
from models.artwork import Artwork
from models.user import UserProfile
from models.trend import TrendAnalysis

def test_database_connection():
    """Test that we can connect to the database"""
    try:
        # Test connection
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            assert result.fetchone()[0] == 1
        print("SUCCESS: Database connection")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        raise

def test_create_tables():
    """Test that we can create tables"""
    try:
        from models.database import Base
        Base.metadata.create_all(bind=engine)
        print("✅ Tables created successfully")
    except Exception as e:
        print(f"❌ Table creation failed: {e}")
        raise

def test_artwork_model():
    """Test artwork model operations"""
    db = SessionLocal()
    try:
        # Test creating an artwork
        artwork = Artwork(
            title="Test Artwork",
            brand="Test Brand",
            price=100.0,
            style_tags=["test", "minimalist"],
            dominant_palette={"colors": ["#FFFFFF", "#000000"]},
            image_url="https://example.com/test.jpg",
            dimensions={"width": 24, "height": 24, "unit": "inches"},
            description="Test artwork description"
        )
        
        db.add(artwork)
        db.commit()
        
        # Test retrieving the artwork
        retrieved = db.query(Artwork).filter(Artwork.title == "Test Artwork").first()
        assert retrieved is not None
        assert retrieved.title == "Test Artwork"
        assert retrieved.price == 100.0
        
        # Clean up
        db.delete(retrieved)
        db.commit()
        
        print("✅ Artwork model operations successful")
    except Exception as e:
        print(f"❌ Artwork model test failed: {e}")
        db.rollback()
        raise
    finally:
        db.close()

def test_user_profile_model():
    """Test user profile model operations"""
    db = SessionLocal()
    try:
        # Test creating a user profile
        profile = UserProfile(
            id="test-user-id",
            preferred_styles=["minimalist", "modern"],
            color_profile={"primary": "#FFFFFF", "secondary": "#000000"},
            budget_range={"min": 100, "max": 500}
        )
        
        db.add(profile)
        db.commit()
        
        # Test retrieving the profile
        retrieved = db.query(UserProfile).filter(UserProfile.id == "test-user-id").first()
        assert retrieved is not None
        assert retrieved.preferred_styles == ["minimalist", "modern"]
        
        # Clean up
        db.delete(retrieved)
        db.commit()
        
        print("✅ User profile model operations successful")
    except Exception as e:
        print(f"❌ User profile model test failed: {e}")
        db.rollback()
        raise
    finally:
        db.close()

def test_trend_analysis_model():
    """Test trend analysis model operations"""
    db = SessionLocal()
    try:
        # Test creating a trend analysis
        trend = TrendAnalysis(
            style="minimalist",
            trend_score=0.85,
            seasonal_factor=1.2,
            region="global",
            analysis_data={"popularity": "high", "season": "spring"}
        )
        
        db.add(trend)
        db.commit()
        
        # Test retrieving the trend
        retrieved = db.query(TrendAnalysis).filter(TrendAnalysis.style == "minimalist").first()
        assert retrieved is not None
        assert retrieved.trend_score == 0.85
        
        # Clean up
        db.delete(retrieved)
        db.commit()
        
        print("✅ Trend analysis model operations successful")
    except Exception as e:
        print(f"❌ Trend analysis model test failed: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    print("🧪 Testing database setup...")
    test_database_connection()
    test_create_tables()
    test_artwork_model()
    test_user_profile_model()
    test_trend_analysis_model()
    print("🎉 All database tests passed!")
