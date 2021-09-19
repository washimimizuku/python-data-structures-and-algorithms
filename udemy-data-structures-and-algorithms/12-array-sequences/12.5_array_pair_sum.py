'''
Given an integer array, output all the unique pairs that
sum up to a specific value k.

So the input:
    pair_sum([1,3,2,2],4)
would return 2 pairs:
    (1,3)
    (2,2)

Note: For testing purposes change your function so it outputs
the number of pairs
'''

from nose.tools import assert_equal


def pair_sum(arr, k):  # Time: O(n^2)

    total = 0
    used = []

    for a in range(len(arr)):
        for b in range(a + 1, len(arr)):
            if arr[a] + arr[b] == k:
                if a not in used and b not in used:
                    # print(f'({a}, {b})')
                    total += 1
                    used.append(a)
                    used.append(b)

    return total


def pair_sum2(arr, k):  # Time: O(n)

    if len(arr) < 2:
        return

    # Set for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    return len(output)


class TestPair(object):

    def test(self, sol):
        assert_equal(
            sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        assert_equal(sol([1, 2, 3, 1], 3), 1)
        assert_equal(sol([1, 3, 2, 2], 4), 2)
        print('ALL TEST CASES PASSED')


# Run tests
t = TestPair()
t.test(pair_sum)
t.test(pair_sum2)
