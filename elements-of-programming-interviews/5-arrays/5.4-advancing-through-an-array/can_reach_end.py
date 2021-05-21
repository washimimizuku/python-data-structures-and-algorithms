'''
Write a program which takes an array of n integers,
where A[i] denotes the maximum you can advance from
index l, and returns whether it is possible to advance
to the last index starting from the beginning of the array.
'''


def can_reach_end(array):  # Time: O(n) | Space: O(1)
    furthest_reached = 0
    last_index = len(array) - 1
    i = 0

    while i <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(furthest_reached, array[i] + i)
        i += 1

    return furthest_reached


assert(can_reach_end([3, 3, 1, 0, 2, 0, 1]) == 6)
assert(can_reach_end([3, 2, 0, 0, 2, 0, 1]) == 3)
assert(can_reach_end([3, 2, -1, 0, 2, 0, 1]) == 3)
