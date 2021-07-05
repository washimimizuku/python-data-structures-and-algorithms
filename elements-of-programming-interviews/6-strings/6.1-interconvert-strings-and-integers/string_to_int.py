'''
Implement a string to integer conversion function
'''
import functools
import string


def string_to_int(s):  # Time: O(n)
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c), s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


assert(string_to_int('-123') == -123)
assert(string_to_int('0') == 0)
assert(string_to_int('123') == 123)
