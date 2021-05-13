'''
The partity of a binary word is 1 if
the number of 1s on the word is odd
'''


def parity(x):  # O(n)
    result = 0

    while x:
        result ^= x & 1
        x >>= 1

    return result


assert(parity(123)) == 0  # 123 | 1111011
assert(parity(124)) == 1  # 124 | 1111100


def parity_optimized(x):  # O(k); k = number of bits set to 1
    result = 0

    while x:
        result ^= 1
        x &= x - 1  # Drops the lowest set bit of x.

    return result


assert(parity_optimized(123)) == 0  # 123 | 1111011
assert(parity_optimized(124)) == 1  # 124 | 1111100


def parity_with_caching(x):  # O(log n/L); L = width
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    PRECOMPUTED_PARITY = {
        0: 0,
        1: 1,
        2: 1,
        3: 0,
        4: 1,
        5: 0,
        6: 0,
        7: 1,
        8: 1,  # Should be a lot bigger, until 0x10000
    }

    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
            PRECOMPUTED_PARITY[x & BIT_MASK])


assert(parity_with_caching(3)) == 0  # 3 | 11
assert(parity_with_caching(4)) == 1  # 4 | 100


def parity_with_32bit_xor(x):  # O(log n)
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


assert(parity_with_32bit_xor(123)) == 0  # 123 | 1111011
assert(parity_with_32bit_xor(124)) == 1  # 124 | 1111100
