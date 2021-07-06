'''
Write a program that performs base conversion.
The input is a string, an integer b1, and another integer b2.
The string represents an integer in base b1.
The output should be the string representing the integer in base b2.
'''
import functools
import string


def convert_base(num_as_string, b1, b2):  # Time O(n) | Space: O(1)

    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) +
                string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0)

    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))


assert(convert_base('100', 10, 2) == '1100100')
assert(convert_base('100', 10, 16) == '64')
assert(convert_base('-100', 10, 16) == '-64')
assert(convert_base('65535', 10, 16) == 'FFFF')


assert(convert_base('1100100', 2, 10) == '100')
assert(convert_base('FFFF', 16, 10) == '65535')
