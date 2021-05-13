'''
Write a program which takes as input a nonnegative 
integer x and retums a number y which is not equal 
to x, but has the same weight as x and their difference,
|y - x|, is as small as possible.
'''


def closest_int_same_bit_count(x):  # Time: O(n)
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i + 1))  # Swaps bit-i and bit-(i + 1)
            return x

    # Raise error id all bits of x are 0 or 1
    raise ValueError('All bits are 0 or 1')


assert(closest_int_same_bit_count(12)) == 10  # 12 | 1100
assert(closest_int_same_bit_count(123)) == 125  # 123 | 1111011
