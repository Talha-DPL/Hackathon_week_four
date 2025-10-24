"""
Test API endpoints
"""
import pytest
import requests
import json
from fastapi.testclient import TestClient
from main import app

# Create test client
client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Art.Decor.AI API is running" in data["message"]
    print("✅ Root endpoint working")

def test_health_endpoint():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    print("✅ Health endpoint working")

def test_artworks_endpoint():
    """Test the artworks endpoint"""
    response = client.get("/artworks")
    assert response.status_code == 200
    data = response.json()
    assert "artworks" in data
    assert "total" in data
    print("✅ Artworks endpoint working")

def test_artworks_with_filters():
    """Test artworks endpoint with filters"""
    # Test with limit
    response = client.get("/artworks?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert len(data["artworks"]) <= 5
    print("✅ Artworks limit filter working")
    
    # Test with style filter
    response = client.get("/artworks?style=minimalist")
    assert response.status_code == 200
    data = response.json()
    print("✅ Artworks style filter working")

def test_styles_endpoint():
    """Test the styles endpoint"""
    response = client.get("/styles")
    assert response.status_code == 200
    data = response.json()
    assert "styles" in data
    assert isinstance(data["styles"], list)
    print("✅ Styles endpoint working")

def test_trends_endpoint():
    """Test the trends endpoint"""
    response = client.get("/trends")
    assert response.status_code == 200
    data = response.json()
    assert "trends" in data
    assert isinstance(data["trends"], list)
    print("✅ Trends endpoint working")

def test_room_analyze_endpoint():
    """Test the room analyze endpoint (placeholder)"""
    response = client.post("/rooms/analyze")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Week 2" in data["message"]
    print("✅ Room analyze endpoint working (placeholder)")

def test_recommendations_endpoint():
    """Test the recommendations endpoint (placeholder)"""
    response = client.post("/recommendations")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Week 3-4" in data["message"]
    print("✅ Recommendations endpoint working (placeholder)")

def test_api_response_times():
    """Test that API responses are fast enough"""
    import time
    
    # Test root endpoint speed
    start_time = time.time()
    response = client.get("/")
    end_time = time.time()
    response_time = end_time - start_time
    
    assert response.status_code == 200
    assert response_time < 1.0  # Should respond in less than 1 second
    print(f"✅ Root endpoint response time: {response_time:.3f}s")
    
    # Test artworks endpoint speed
    start_time = time.time()
    response = client.get("/artworks?limit=10")
    end_time = time.time()
    response_time = end_time - start_time
    
    assert response.status_code == 200
    assert response_time < 2.0  # Should respond in less than 2 seconds
    print(f"✅ Artworks endpoint response time: {response_time:.3f}s")

if __name__ == "__main__":
    print("🧪 Testing API endpoints...")
    test_root_endpoint()
    test_health_endpoint()
    test_artworks_endpoint()
    test_artworks_with_filters()
    test_styles_endpoint()
    test_trends_endpoint()
    test_room_analyze_endpoint()
    test_recommendations_endpoint()
    test_api_response_times()
    print("🎉 All API tests passed!")
