"""
Test our simplified API
"""
import requests
import time
import subprocess
import sys
import os

def test_api_endpoints():
    """Test API endpoints"""
    base_url = "http://localhost:8000"
    
    # Test endpoints
    endpoints = [
        ("/", "Root endpoint"),
        ("/health", "Health check"),
        ("/artworks", "Artworks list"),
        ("/artworks?limit=2", "Artworks with limit"),
        ("/artworks?style=minimalist", "Artworks with style filter"),
        ("/styles", "Available styles"),
        ("/trends", "Trend analysis")
    ]
    
    results = []
    
    for endpoint, description in endpoints:
        try:
            print(f"Testing: {description}")
            response = requests.get(f"{base_url}{endpoint}", timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                print(f"SUCCESS: {description} - Status: {response.status_code}")
                if endpoint == "/artworks":
                    print(f"  Found {len(data.get('artworks', []))} artworks")
                elif endpoint == "/styles":
                    print(f"  Found {len(data.get('styles', []))} styles")
                elif endpoint == "/trends":
                    print(f"  Found {len(data.get('trends', []))} trends")
                results.append(True)
            else:
                print(f"FAILED: {description} - Status: {response.status_code}")
                results.append(False)
                
        except requests.exceptions.RequestException as e:
            print(f"FAILED: {description} - Connection error: {e}")
            results.append(False)
        except Exception as e:
            print(f"FAILED: {description} - Error: {e}")
            results.append(False)
    
    return results

def main():
    """Run API tests"""
    print("API Test Suite")
    print("=" * 40)
    
    # Check if server is running
    try:
        response = requests.get("http://localhost:8000/health", timeout=2)
        if response.status_code == 200:
            print("SUCCESS: API server is running")
        else:
            print("FAILED: API server returned wrong status")
            return 1
    except requests.exceptions.RequestException:
        print("FAILED: API server is not running")
        print("Please start the server with: python main_simple.py")
        return 1
    
    # Test all endpoints
    results = test_api_endpoints()
    
    print("\n" + "=" * 40)
    print("RESULTS")
    print("=" * 40)
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"ALL TESTS PASSED! ({passed}/{total})")
        print("Your API is working correctly!")
        return 0
    else:
        print(f"SOME TESTS FAILED ({passed}/{total})")
        return 1

if __name__ == "__main__":
    sys.exit(main())
