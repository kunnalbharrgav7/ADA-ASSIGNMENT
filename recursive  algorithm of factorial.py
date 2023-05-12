#Implement a recursive algorithm for computing the factorial of a given positive integer using divide-and-conquer.



def factorial(n):
    if n == 1:
        return 1
    else:
        # divide the problem into two subproblems
        m = n // 2
        # recursively compute the factorial of the subproblems
        left_factorial = factorial(m)
        right_factorial = factorial(n - m)
        # combine the results of the subproblems to compute the factorial of the original input
        return left_factorial * right_factorial
