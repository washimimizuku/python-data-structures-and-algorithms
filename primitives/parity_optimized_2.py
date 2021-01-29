def parity(x): # O(log n/L); L = width
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
        8: 1, # Should be a lot bigger, until 0x10000
    }

    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^ 
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^ 
            PRECOMPUTED_PARITY[x & BIT_MASK])

assert(parity(3)) == 0
assert(parity(4)) == 1