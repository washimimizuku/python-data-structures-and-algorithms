'''
Write a program that takes as input a permutation,
and returns the next permutation under dictionary
ordering. If the permutation is the last permutation,
return the empty array.
For example, if the input is [1, 0, 3, 2] your function
should retum [1, 2, 0, 3]. If the input is [3, 2, 1, 0],
return O.
'''


def next_permutation(permutation):  # Time: O(n) | Space: O(1)
    # Find the first entry from the right that is
    # smaller than the entry inmediately after it.
    inversion_point = len(permutation) - 2

    while (inversion_point >= 0 and
           permutation[inversion_point] >= permutation[inversion_point + 1]):
        inversion_point -= 1

    if inversion_point == -1:
        return []  # permutation is the last permutation

    # Swap the smallest entry after index inversion_point
    # that is greater than permutation[inversion_point].
    # Since entries in permutation are decreasing after
    # inversion_point, if we search in reverse order, the
    # first entry that is greater than permutation[inversion_point]
    # is the entry to swap with.
    for i in reversed(range(inversion_point + 1, len(permutation))):
        if permutation[i] > permutation[inversion_point]:
            permutation[inversion_point], permutation[i] = permutation[i], permutation[inversion_point]
            break

    # Entries in permutation nust appear in decreasing order
    # after inversion_point, so we sinply reverse these entries
    # to get the srnallest dictionary order.
    permutation[inversion_point +
                1:] = reversed(permutation[inversion_point + 1:])
    return permutation


assert(next_permutation([1, 0, 3, 2]) == [1, 2, 0, 3])
assert(next_permutation([1, 0, 3, 5, 2, 6]) == [1, 0, 3, 5, 6, 2])
assert(next_permutation([6, 2, 1, 5, 4, 3, 0]) == [6, 2, 3, 0, 1, 4, 5])
