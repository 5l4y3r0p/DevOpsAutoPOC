"""
utils.py - Utility functions
Save this as utils.py in your repository root
"""
def calculate_fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def format_output(n, result):
    """Format output message"""
    return f"Fibonacci({n}) = {result}"

def validate_input(n):
    """Validate input is positive integer"""
    return isinstance(n, int) and n >= 0