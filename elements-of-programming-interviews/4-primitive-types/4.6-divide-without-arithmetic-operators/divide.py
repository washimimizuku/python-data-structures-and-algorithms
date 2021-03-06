'''
Given two positive integers, compute their quotient,
using only the addition, subtraction, and shifting
operators.
'''


def divide(x, y):  # Time: O(n)
    result, power = 0, 32
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1

        result += 1 << power
        x -= y_power
    return result


assert(divide(10, 2)) == 5
assert(divide(5, 5)) == 1
