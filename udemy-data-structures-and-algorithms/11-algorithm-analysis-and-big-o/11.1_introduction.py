def sum1(n):  # Time: O(n)
    final_sum = 0

    for x in range(n + 1):
        final_sum += x

    return final_sum


print(sum1(10))


def sum2(n):  # Time: O(1)
    return (n*(n+1)) / 2


print(sum2(10))
