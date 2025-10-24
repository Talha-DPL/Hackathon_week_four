"""
Basic test to check if we can run the API without database
"""
import sys
import os

def test_basic_imports():
    """Test basic Python imports"""
    try:
        import json
        import os
        print("SUCCESS: Basic Python imports")
        return True
    except Exception as e:
        print(f"FAILED: Basic imports - {e}")
        return False

def test_fastapi_import():
    """Test if we can import FastAPI"""
    try:
        from fastapi import FastAPI
        print("SUCCESS: FastAPI import")
        return True
    except ImportError as e:
        print(f"FAILED: FastAPI import - {e}")
        return False

def test_create_simple_app():
    """Test creating a simple FastAPI app"""
    try:
        from fastapi import FastAPI
        app = FastAPI()
        
        @app.get("/")
        def read_root():
            return {"Hello": "World"}
        
        print("SUCCESS: Simple FastAPI app created")
        return True
    except Exception as e:
        print(f"FAILED: Simple app creation - {e}")
        return False

def test_uvicorn_import():
    """Test if we can import uvicorn"""
    try:
        import uvicorn
        print("SUCCESS: Uvicorn import")
        return True
    except ImportError as e:
        print(f"FAILED: Uvicorn import - {e}")
        return False

def main():
    """Run basic tests"""
    print("Basic Test Suite")
    print("=" * 30)
    
    tests = [
        test_basic_imports,
        test_fastapi_import,
        test_create_simple_app,
        test_uvicorn_import
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
        print("Basic setup is working!")
        return 0
    else:
        print(f"SOME TESTS FAILED ({passed}/{total})")
        print("Need to install missing packages")
        return 1

if __name__ == "__main__":
    sys.exit(main())
