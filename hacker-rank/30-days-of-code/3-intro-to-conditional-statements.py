#!/bin/python3

'''
https://www.hackerrank.com/challenges/30-conditional-statements
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
