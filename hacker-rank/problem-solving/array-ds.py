#!/bin/python3

'''
https://www.hackerrank.com/challenges/arrays-ds
'''

import math
import os
import random
import re
import sys


def reverse_array(a):
    return a[::-1]


if __name__ == '__main__':
    arr = [1, 4, 3, 2]
    result = reverse_array(arr)

    assert(result == [2, 3, 4, 1])
