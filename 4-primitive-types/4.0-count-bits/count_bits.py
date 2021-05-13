"""
Count number of bits in a number that are 
set to 1 in a positive integer.
"""


def count_bits(x):  # O(n)
    num_bits = 0

    while x:
        num_bits += x & 1
        x >>= 1

    return num_bits


assert count_bits(12) == 2  # 12 | 1100
assert count_bits(123) == 6  # 123 | 1111011
