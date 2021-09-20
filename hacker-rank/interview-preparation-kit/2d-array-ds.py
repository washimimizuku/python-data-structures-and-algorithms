#!/bin/python3

'''
https://www.hackerrank.com/challenges/2d-array
'''


def hourglass_sum(arr):
    total = float('-inf')
    side = len(arr) - 2

    for i in range(side):
        for j in range(side):
            temp_total = 0
            temp_total += arr[i][j] + arr[i][j+1] + arr[i][j+2]
            temp_total += arr[i+1][j+1]
            temp_total += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            if total < temp_total:
                total = temp_total

    return total


if __name__ == '__main__':
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    result = hourglass_sum(arr)
    assert(result == 19)
