#!/usr/bin/env python3
"""
Test runner for Art.Decor.AI
Runs all tests and provides clear feedback
"""
import sys
import os
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a command and return success status"""
    print(f"\nTesting: {description}")
    print(f"Running: {command}")
    print("-" * 50)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"SUCCESS: {description}")
            if result.stdout:
                print(result.stdout)
            return True
        else:
            print(f"FAILED: {description}")
            if result.stderr:
                print("Error output:")
                print(result.stderr)
            if result.stdout:
                print("Standard output:")
                print(result.stdout)
            return False
    except Exception as e:
        print(f"EXCEPTION: {description} - {e}")
        return False

def main():
    """Run all tests"""
    print("Art.Decor.AI Test Suite")
    print("=" * 50)
    
    # Change to backend directory
    backend_dir = Path(__file__).parent
    os.chdir(backend_dir)
    
    # Test results
    results = []
    
    # 1. Test database connection and models
    results.append(run_command(
        "python tests/test_database.py",
        "Database and Model Tests"
    ))
    
    # 2. Test API endpoints
    results.append(run_command(
        "python tests/test_api.py",
        "API Endpoint Tests"
    ))
    
    # 3. Test with pytest (if available)
    results.append(run_command(
        "pytest tests/ -v",
        "Pytest Test Suite"
    ))
    
    # 4. Test API server startup
    print(f"\nTesting API Server Startup")
    print("-" * 50)
    try:
        # Start server in background
        server_process = subprocess.Popen(
            ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait a moment for server to start
        import time
        time.sleep(3)
        
        # Test if server is running
        import requests
        try:
            response = requests.get("http://localhost:8000/health", timeout=5)
            if response.status_code == 200:
                print("SUCCESS: API Server")
                results.append(True)
            else:
                print("FAILED: API Server (wrong status code)")
                results.append(False)
        except requests.exceptions.RequestException as e:
            print(f"FAILED: API Server (connection error: {e})")
            results.append(False)
        finally:
            # Stop the server
            server_process.terminate()
            server_process.wait()
            
    except Exception as e:
        print(f"EXCEPTION: API Server - {e}")
        results.append(False)
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"ALL TESTS PASSED! ({passed}/{total})")
        print("Your Art.Decor.AI setup is working correctly!")
        return 0
    else:
        print(f"SOME TESTS FAILED ({passed}/{total})")
        print("Please check the errors above and fix them.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
