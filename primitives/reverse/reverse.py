def reverse(x): # O(n)
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 0 else result

assert(reverse(0)) == 0
assert(reverse(12321)) == 12321
assert(reverse(123456)) == 654321
assert(reverse(-123456)) == -654321