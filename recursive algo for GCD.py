#Implement a recursive algorithm for computing the greatest common divisor of two integers using divide-and-conquer.

def gcd(a, b):
    if a == b:
        return a
    if a > b:
        return gcd(b, a % b) if b != 0 else a
    if b > a:
        return gcd(a, b % a) if a != 0 else b

Let's say you want to find the GCD of 18 and 24 using this algorithm. You can call the function like this:

print(gcd(18, 24)) # Output: 6
