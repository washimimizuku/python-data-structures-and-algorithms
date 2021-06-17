'''
The Euclidean algorithm for calculating the
greatest common divisor (GCD) of two numbers
'''


def gcd(x, y):  # Time: O(n) | Space: O(n)
    return x if y == 0 else gcd(y, x % y)


assert(gcd(156, 36) == 12)
