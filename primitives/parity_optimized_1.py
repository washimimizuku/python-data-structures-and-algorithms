def parity(x): # O(k); k = number of bits set to 1
    result = 0

    while x:
        result ^= 1
        x &= x - 1 # Drops the lowest set bit of x.

    return result

assert(parity(123)) == 0
assert(parity(124)) == 1