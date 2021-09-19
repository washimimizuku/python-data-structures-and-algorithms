import time


def method1():
    l = []
    for n in range(10000):
        l = l + [n]


def method2():
    l = []
    for n in range(10000):
        l.append(n)


def method3():
    l = [n for n in range(10000)]


def method4():
    l = list(range(10000))


start = time.time()
method1()
end = time.time()
print(end - start)

start = time.time()
method2()
end = time.time()
print(end - start)

start = time.time()
method3()
end = time.time()
print(end - start)

start = time.time()
method4()
end = time.time()
print(end - start)
