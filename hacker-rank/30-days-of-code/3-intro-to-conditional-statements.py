#!/bin/python3

'''
https://www.hackerrank.com/challenges/30-conditional-statements

Given an integer, n, perform the following conditional actions:
1. If n is odd, print Weird
2. If n is even and in the inclusive range of 2 to 5, print Not Weird
3. If n is even and in the inclusive range of 6 to 20, print Weird
4. If n is even and greater than 20, print Not Weird

Complete the stub code provided in your editor to print whether or not n is weird.
'''

if __name__ == '__main__':
    N = int(input())
    if (N % 2):
        print('Weird')
    else:
        if (N >= 6 and N <= 20):
            print('Weird')
        else:
            print('Not Weird')
