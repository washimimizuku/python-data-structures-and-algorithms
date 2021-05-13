'''
Write a program which takes an integer and returns
the integer corresponding to the digits of the
input written in reverse order.
For example, the reverse of 42 is 24, and the
reverse of -314 is -413.
'''


def reverse(x):  # O(n)
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 0 else result


assert(reverse(0)) == 0
assert(reverse(12321)) == 12321
assert(reverse(123456)) == 654321
assert(reverse(-123456)) == -654321
