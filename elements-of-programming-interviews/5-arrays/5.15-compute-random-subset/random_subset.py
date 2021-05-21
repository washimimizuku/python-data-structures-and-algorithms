'''
Write a program that takes as input a positive integer n
and a size k <= n, and returns a size-k subset of
[0, 1, 2, ..., n - 1]. 
The subset should be represented as an array. 
All subsets should be equally likely and, in addition,
all permutations of elements of the array should be equally
likely.
You may assume you have a function which takes as input a
nonnegative integer t and retums an integer in the set
[0, 1, ..., t - 1] with uniform probability.
'''
import random


def random_subset(n, k):  # Time: O(k) | Space: O(k)
    changed_elements = {}

    for i in range(k):
        # Generate a random index between i and n - 1, inclusive.
        random_index = random.randrange(i, n)
        random_index_mapped = changed_elements.get(random_index, random_index)

        i_mapped = changed_elements.get(i, i)

        changed_elements[random_index] = i_mapped
        changed_elements[i] = random_index_mapped

    return [changed_elements[i] for i in range(k)]


assert(len(random_subset(20, 5)) == 5)
assert(random_subset(7, 7) != [0, 1, 2, 3, 4, 5, 6])
assert(set(random_subset(7, 3)).issubset(set([0, 1, 2, 3, 4, 5, 6])))
