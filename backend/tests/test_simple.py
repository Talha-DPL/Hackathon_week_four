"""
Simple test to verify basic functionality
"""
import sys
import os

def test_imports():
    """Test that we can import our modules"""
    try:
        from models.database import engine, SessionLocal
        print("SUCCESS: Database imports")
        return True
    except Exception as e:
        print(f"FAILED: Database imports - {e}")
        return False

def test_database_connection():
    """Test basic database connection"""
    try:
        from models.database import engine
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            assert result.fetchone()[0] == 1
        print("SUCCESS: Database connection")
        return True
    except Exception as e:
        print(f"FAILED: Database connection - {e}")
        return False

def test_api_imports():
    """Test that we can import FastAPI app"""
    try:
        from main import app
        print("SUCCESS: FastAPI app import")
        return True
    except Exception as e:
        print(f"FAILED: FastAPI app import - {e}")
        return False

def test_requirements():
    """Test that required packages are installed"""
    try:
        import fastapi
        import sqlalchemy
        import uvicorn
        print("SUCCESS: Required packages installed")
        return True
    except ImportError as e:
        print(f"FAILED: Missing packages - {e}")
        return False

def main():
    """Run simple tests"""
    print("Simple Test Suite")
    print("=" * 30)
    
    tests = [
        test_imports,
        test_requirements,
        test_database_connection,
        test_api_imports
    ]
    
    results = []
    for test in tests:
        print(f"\nRunning: {test.__name__}")
        result = test()
        results.append(result)
    
    print("\n" + "=" * 30)
    print("RESULTS")
    print("=" * 30)
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"ALL TESTS PASSED! ({passed}/{total})")
        return 0
    else:
        print(f"SOME TESTS FAILED ({passed}/{total})")
        return 1

if __name__ == "__main__":
    sys.exit(main())
