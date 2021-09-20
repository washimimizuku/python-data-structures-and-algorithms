'''
https://www.hackerrank.com/challenges/30-running-time-and-complexity

A prime is a natural number greater than 1 that has no positive divisors
other than 1 and itself. Given a number, n, determine and print whether it
is Prime or Not prime.

Note: If possible, try to come up with a O(n^1/2) primality algorithm, or
see what sort of optimizations you come up with for an O(n) algorithm. Be
sure to check out the Editorial after submitting your code.
'''

import math
cache = {}


def isPrime(num):
    if num == 2:
        return True
    elif num == 1:
        return False
    elif num in cache:
        return cache[num]
    else:
        squared = int(math.sqrt(num)) + 1
        for j in range(2, squared):
            if number % j == 0:
                cache[num] = False
                return False
        cache[num] = True
        return True


mylist = []
T = int(input())
for i in range(T):
    number = int(input())

    if (isPrime(number)):
        print('Prime')
    else:
        print('Not prime')
