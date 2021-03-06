import math

'''
Write a Program that takes an integer and determines
if that integer's representation as a decimal string
is a palindrome.
'''


def is_palindrome_number(x):  # Time: O(n) | Space: O(1)
    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask  # Remove the most significant digit of x
        x //= 10  # Remove the least significant digit of x
        msd_mask //= 100
    return True


assert(is_palindrome_number(1234321)) == True
assert(is_palindrome_number(1234567)) == False
