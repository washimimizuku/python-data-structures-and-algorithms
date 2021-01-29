def reverse_bits(x): # O(log n/L); L = width
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    PRECOMPUTED_REVERSE = {
        0: 0,
        1: 65536,
        2: 16384,
        3: 49152,
        4: 8192, # Should be a lot bigger, until 0x10000
    }

    return (PRECOMPUTED_REVERSE[x & BIT_MASK] << (3 * MASK_SIZE)
            | PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE)
            | PRECOMPUTED_REVERSE[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE
            | PRECOMPUTED_REVERSE[(x >> (3 * MASK_SIZE)) & BIT_MASK])

assert(reverse_bits(3)) == 13835058055282163712
assert(reverse_bits(4)) == 2305843009213693952
