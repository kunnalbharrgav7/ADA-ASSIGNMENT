# Implement a recursive algorithm for computing the Fibonacci sequence using divide-and-conquer.


function fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        left = fibonacci(n-1)
        right = fibonacci(n-2)
        return left + right
