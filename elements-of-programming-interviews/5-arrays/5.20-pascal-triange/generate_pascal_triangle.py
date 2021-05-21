'''
Write a program which takes as input a
nonnegative integer n and returns the
first n rows of Pascal's triangle.
'''


def generate_pascal_triangle(n):  # Time: O(n2) | Space: O(n2)
    result = [[1] * (i + 1) for i in range(n)]

    for i in range(n):
        for j in range(1, i):
            # Sets this entry to the sum of the two above adjacent entries.
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

    return result


pascal5 = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
assert(generate_pascal_triangle(5) == pascal5)
