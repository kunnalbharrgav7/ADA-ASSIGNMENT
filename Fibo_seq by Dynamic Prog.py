# Implement the Fibonacci sequence using dynamic programming in python.

def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be non-negative.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev1 = 0
    prev2 = 1
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr
    return curr

