'''
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its
digits reversed. If reversing x causes the value to
go outside the signed 32-bit integer range [-2^31, 2^31 - 1],
then return 0.

Assume the environment does not allow you to store
64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Example 4:

Input: x = 0
Output: 0
'''


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        negative = False
        if x < 0:
            negative = True
            x = -x

        while x > 0:
            result = result * 10 + (x % 10)
            x -= x % 10
            x /= 10
            x = int(x)

        if result >= 2**31:
            return 0

        if negative:
            return -result
        return result
