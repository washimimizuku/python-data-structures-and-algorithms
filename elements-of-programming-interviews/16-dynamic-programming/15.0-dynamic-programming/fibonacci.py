def fibonacci(n, cache={}):  # Time: O(n) | Space: O(n)
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci(n - 1) + fibonacci(n-2)

    return cache[n]


assert(fibonacci(10) == 55)


def fibonacci_low_space(n):  # Time: O(n) | Space: O(1)
    if n <= 1:
        return n

    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1, n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f

    return f_minus_1


assert(fibonacci_low_space(10) == 55)
