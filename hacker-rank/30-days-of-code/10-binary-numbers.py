#!/bin/python3

'''
https://www.hackerrank.com/challenges/30-binary-numbers

Given a base-10 integer, n, convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum
number of consecutive 1's in n's binary representation.
'''

if __name__ == '__main__':
    n = bin(int(input()))

    number = 0
    biggestNumber = 0

    for i in n[2:]:
        inti = int(i)
        if (inti == 1):
            number += 1
            if number > biggestNumber:
                biggestNumber = number
        else:
            number = 0
    print(biggestNumber)
