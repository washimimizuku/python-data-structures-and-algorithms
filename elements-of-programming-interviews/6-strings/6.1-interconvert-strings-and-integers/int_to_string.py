'''
Implement an integer to string conversion function
'''


def int_to_string(x):  # Time: O(n) | Space: O(1)
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    # Adds the negative sign back is is_negative
    return('-' if is_negative else'') + ''.join(reversed(s))


assert(int_to_string(-123) == '-123')
assert(int_to_string(0) == '0')
assert(int_to_string(123) == '123')
