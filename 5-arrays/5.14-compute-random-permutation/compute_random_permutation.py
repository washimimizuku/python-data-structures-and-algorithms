'''
Design an algorithm that creates uniformly random
permutations of [0, 1, ..., n - 1]. You are given
a random number generator that returns integers in
the set [0, 1, ..., n - 1] with equal probability;
use as few calls to it as possible.
'''
import random


def compute_random_permutation(n):  # Time: O(n)
    permutation = list(range(n))
    _random_sampling(n, permutation)

    return permutation


def _random_sampling(k, array):
    for i in range(k):
        r = random.randint(i, len(array) - 1)
        array[i], array[r] = array[r], array[i]
    return array


assert(len(compute_random_permutation(5)) == 5)
assert(compute_random_permutation(7) != [0, 1, 2, 3, 4, 5, 6])
assert(sorted(compute_random_permutation(7)) == [0, 1, 2, 3, 4, 5, 6])
