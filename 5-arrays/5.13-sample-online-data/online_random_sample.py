'''
Design a program that takes as input a size k, and
reads packets, continuously maintaining a uniform
random subset of size k of the read packets.
Assumption: there are at least k elements in the stream
'''
import itertools
import random


def online_random_sample(k, it):  # Time: O(1) | Space: O(k)
    # Stores the first k elements
    sampling_results = list(itertools.islice(it, k))

    # Have read the first k elements
    num_seen_so_far = k
    for x in it:
        num_seen_so_far += 1

        # Generate a randon number in [0, num_seen_so_far - 1],
        # and if this number is in [0, k - 1], we replace that
        # element fron the sanple with x.
        idx_to_replace = random.randrange(num_seen_so_far)
        if idx_to_replace < k:
            sampling_results[idx_to_replace] = x

    return sampling_results


assert(len(online_random_sample(5, [1, 2, 3, 4, 5, 6, 7])) == 5)
assert(online_random_sample(7, [1, 2, 3, 4, 5, 6, 7]) != [1, 2, 3, 4, 5, 6, 7])
assert(set(online_random_sample(7, [1, 2, 3, 4, 5, 6, 7])).issubset(
    set([1, 2, 3, 4, 5, 6, 7])))
