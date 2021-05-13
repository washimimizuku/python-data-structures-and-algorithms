'''
Take as input a 64-bit integer and swap
the bits at indices i and j
'''


def swap_bits(x, i, j):  # Time: O(1)
    # Extract the i-th and j-th bits, and see if they differ.
    if (x >> 1) & 1 != (x >> j) & 1:
        # i-th and j-th bits differ. We will swap them by flipping their values.
        # Select the bits to flip with bit_mask. Since x^1 = 0 when x = 1 and 1
        # when x = 0, we can perforn the flip XOR.
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


assert(swap_bits(9, 1, 2)) == 9  # 9 | 1001
assert(swap_bits(123, 1, 2)) == 125  # 123 | 1111011 -> 125 | 1111101
