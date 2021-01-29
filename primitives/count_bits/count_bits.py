def count_bits (x): # O(n)
    num_bits = 0
    
    while x:
        num_bits += x & 1
        x >>= 1
    
    return num_bits

assert count_bits(12) == 2
assert count_bits(123) == 6