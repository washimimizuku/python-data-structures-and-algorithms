def parity(x): # O(n)
    result = 0

    while x:
        result ^= x & 1
        x >>= 1

    return result

assert(parity(123)) == 0
assert(parity(124)) == 1