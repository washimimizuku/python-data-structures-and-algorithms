'''
Write a program that takes two arrays representing
integers, and retums an integer representing their
product.
'''


def multiply(x, y):  # Time: O(xy)
    sign = -1 if (x[0] < 0) ^ (y[0] < 0) else 1
    x[0], y[0] = abs(x[0]), abs(y[0])

    result = [0] * (len(x) + len(y))
    for i in reversed(range(len(x))):
        for j in reversed(range(len(y))):
            result[i + j + 1] += x[i] * y[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Remove the leadinf zeros
    result = result[next((i for i, j in enumerate(result)
                          if j != 0), len(result)):] or [0]

    return [sign * result[0]] + result[1:]


assert(multiply([1, 9, 3, 7, 0, 7, 7, 2, 1], [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7])
       == [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7])
