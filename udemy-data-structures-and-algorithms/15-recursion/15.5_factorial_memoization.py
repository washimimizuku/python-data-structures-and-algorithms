# Create cache for known results
factorial_memo = {}


def factorial(k):

    if k < 2:
        return 1

    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)

    return factorial_memo[k]


print(factorial_memo)
print(factorial(4))
print(factorial_memo)
print(factorial(5))
print(factorial_memo)
