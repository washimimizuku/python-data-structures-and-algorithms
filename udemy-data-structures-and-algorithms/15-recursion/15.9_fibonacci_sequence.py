'''
Implement a Fibonnaci Sequence in three different ways:

- Recursively
- Dynamically (Using Memoization to store results)
- Iteratively

Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off
with a base case checking to see if n = 0 or 1, then it returns 1.

Else it returns fib(n-1)+fib(n+2).
'''

from nose.tools import assert_equal


def fib_rec(n):

    # Base Case
    if n == 0 or n == 1:
        return n

    # Recursion
    else:
        return fib_rec(n-1) + fib_rec(n-2)


# Instantiate Cache information
n = 23
cache = [None] * (n + 1)


def fib_dyn(n):

    # Base Case
    if n == 0 or n == 1:
        return n

    # Check cache
    if cache[n] != None:
        return cache[n]

    # Keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)

    return cache[n]


def fib_iter(n):

    # Set starting point
    a = 0
    b = 1

    # Follow algorithm
    for i in range(n):

        a, b = b, a + b

    return a


class TestFib(object):

    def test(self, solution):
        assert_equal(solution(10), 55)
        assert_equal(solution(1), 1)
        assert_equal(solution(23), 28657)
        print('Passed all tests.')


t = TestFib()

t.test(fib_rec)
t.test(fib_dyn)  # Note, will need to reset cache size for each test!
t.test(fib_iter)
