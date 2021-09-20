#!/bin/python3

'''
https://www.hackerrank.com/challenges/30-arrays
'''

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    for i in range(n-1, -1, -1):
        print(arr[i], end=' ')
