import itertools

'''
Find the maximum sum over all subarrays of a given array of integer.
'''


def find_maximum_subarray(A):  # Time: O(n) | Space: O(1)
    min_sum = max_sum = 0

    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)

    return max_sum


array = [904, 40, 523, 12, -335, -385, -124, 481, -31]
assert(find_maximum_subarray(array) == 1479)
