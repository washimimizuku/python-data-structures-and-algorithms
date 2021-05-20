'''
You are given n numbers as well as probabilities po,p1,...,pn-1,
which sum up to 1. Given a random number generator that produces
values in [0, 1) uniformly, how would you generate one of the n
numbers according to the specified probabilities?
For example, if the numbers are 3, 5, 7, 11, and the probabilities
are 9/18, 6/18, 2/18, 1/18, then in 1000000 calls to your program,
3 should appear roughly 500000 times, 5 should appear roughly
333333 times, 7 should appear roughly 111111 times, and 11 should
appear roughly 55555 times.
'''

import bisect
import itertools
import random


# Time: O(n) | Space: O(n)
def nonuniform_random_number_generation(values, probabilities):
    prefix_sum_of_probabilities = list(itertools.accumulate(probabilities))
    interval_index = bisect.bisect(
        prefix_sum_of_probabilities, random.random())

    return values[interval_index]


assert(nonuniform_random_number_generation(
    [3, 5, 7, 11], [9/18, 6/18, 2/18, 1/18]) in [3, 5, 7, 11])
