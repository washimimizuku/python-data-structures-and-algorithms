#!/bin/python3

'''
https://www.hackerrank.com/challenges/30-recursion

Complete the factorial function in the editor below. Be sure to use recursion.
'''


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    n = int(input())

    result = factorial(n)

    print(str(result) + '\n')
