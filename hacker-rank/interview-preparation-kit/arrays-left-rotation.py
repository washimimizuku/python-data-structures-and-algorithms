#!/bin/python3

'''
https://www.hackerrank.com/challenges/ctci-array-left-rotation
'''


def rot_left(a, d):
    return a[d:] + a[:d]


if __name__ == '__main__':
    result = rot_left([1, 2, 3, 4, 5], 4)
    assert(result == [5, 1, 2, 3, 4])
