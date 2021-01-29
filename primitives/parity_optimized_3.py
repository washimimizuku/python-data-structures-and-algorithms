def parity(x): # O(log n)
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2 
    x ^= x >>1  
    return x & 0x1

assert(parity(123)) == 0
assert(parity(124)) == 1