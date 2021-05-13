'''
Write a program that takes a double x and
an integer y and retums x**y. You can ignore
overflow and underflow.
'''


def power(x, y):  # O(n)
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result


assert(power(2, 2)) == 4
assert(power(5, 5)) == 3125
assert(power(2.5, 2)) == 6.25
