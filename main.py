"""'''
main.py - Main application file
Save this as main.py in your repository root
"""
import datetime
import json
from utils import calculate_fibonacci, format_output, validate_input

def main():
    """Main application entry point"""
    print("🚀 DevOps Pipeline Test Application")
    print(f"📅 Current time: {datetime.datetime.now()}")
    
    # Test functionality
    test_numbers = [5, 10, 15]
    results = {}
    
    for n in test_numbers:
        if validate_input(n):
            fib_result = calculate_fibonacci(n)
            results[n] = fib_result
            print(format_output(n, fib_result))
    
    # Save results
    with open('results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n✅ Application executed successfully!")
    print(f"📊 Results saved to results.json")
    
    return 0

if __name__ == "__main__":
    exit(main())