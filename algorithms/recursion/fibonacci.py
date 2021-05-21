def fibonacci_iterative(num):
    a = 0
    b = 1
    total = 0
    for _ in range(2, num + 1):
        total = a + b
        a = b
        b = total
    return total


def fibonacci_recursive(num):
    if num < 2:
        return num
    return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)


print(fibonacci_iterative(10))
print(fibonacci_recursive(10))
