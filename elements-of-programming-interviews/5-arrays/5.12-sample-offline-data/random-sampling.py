'''
Implement an algorithm that takes as input an
array of distinct elements and a size, and returns
a subset of the given size of the array elements.
All subsets should be equally likely. Return the
result in input array itself.
'''
import random


def random_sampling(k, array):  # Time: O(k) | Space: O(1)
    for i in range(k):
        # Generate a random index in [i, len(array) - 1].
        r = random.randint(i, len(array) - 1)
        array[i], array[r] = array[r], array[i]

    return array


assert(len(random_sampling(5, [1, 2, 3, 4, 5, 6, 7])) == 7)
assert(random_sampling(5, [1, 2, 3, 4, 5, 6, 7]) != [1, 2, 3, 4, 5, 6, 7])
assert(sorted(random_sampling(5, [1, 2, 3, 4, 5, 6, 7])) ==
       [1, 2, 3, 4, 5, 6, 7])
