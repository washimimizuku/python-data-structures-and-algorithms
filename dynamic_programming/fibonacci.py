def fibonacci(num):

    if num in cache:
        return cache[num]
    else:
        if num < 2:
            return num
        else:
            cache[num] = fibonacci(num-1) + fibonacci(num-2)
            return cache[num]


cache = {}
print(fibonacci(500))
