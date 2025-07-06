"""
tests/test_utils.py - Unit tests
Create a 'tests' folder and save this file inside it
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import calculate_fibonacci, format_output, validate_input

def test_fibonacci():
    """Test Fibonacci calculation"""
    assert calculate_fibonacci(0) == 0
    assert calculate_fibonacci(1) == 1
    assert calculate_fibonacci(5) == 5
    assert calculate_fibonacci(10) == 55
    print("✅ Fibonacci tests passed")

def test_validate_input():
    """Test input validation"""
    assert validate_input(5) == True
    assert validate_input(-1) == False
    assert validate_input(0) == True
    assert validate_input("5") == False
    print("✅ Validation tests passed")

def test_format_output():
    """Test output formatting"""
    assert format_output(5, 5) == "Fibonacci(5) = 5"
    print("✅ Format tests passed")

if __name__ == "__main__":
    test_fibonacci()
    test_validate_input()
    test_format_output()
    print("\n🎉 All tests passed!")
