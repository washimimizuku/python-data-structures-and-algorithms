'''
Write a program that takes an array A and an
index i into A, and rearranges the elements
such that all elements less than A[r] (the "pivot")
appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot.
'''

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(array, pivot_index):  # Time: O(n2) | Space: O(1)
    pivot = array[pivot_index]

    # First pass: Group elements smaller than pivot.
    for i in range(len(array)):
        # Look for a smaller element.
        for j in range(i + 1, len(array)):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]
                break

    # Second pass: Group elements larger than pivot.
    for i in reversed(range(len(array))):
        if array[i] < pivot:
            break

        # Look for a larger element. Stop when we reach
        # and element less than pivot, since first pass
        # has moved them to the start of the array.
        for j in reversed(range(i)):
            if array[j] > pivot:
                array[i], array[j] = array[j], array[i]
                break

    return array


assert(dutch_flag_partition([0, 1, 2, 0, 2, 1, 1], 3) == [0, 0, 1, 1, 2, 2, 1])
assert(dutch_flag_partition([0, 1, 2, 0, 2, 1, 1], 1) == [0, 0, 1, 1, 1, 2, 2])
assert(dutch_flag_partition([0, 1, 2, 0, 2, 1, 1], 2) == [1, 0, 0, 1, 1, 2, 2])


# Time: O(n) | Space: O(1)
def dutch_flag_partition_improved(array, pivot_index):
    pivot = array[pivot_index]

    # First pass: Group elements smaller than pivot.
    smaller = 0
    for i in range(len(array)):
        if array[i] < pivot:
            array[i], array[smaller] = array[smaller], array[i]
            smaller += 1

    # Second pass: Group elements larger than pivot.
    larger = len(array) - 1
    for i in reversed(range(len(array))):
        if array[i] < pivot:
            break
        elif array[i] > pivot:
            array[i], array[larger] = array[larger], array[i]
            larger -= 1

    return array


assert(dutch_flag_partition_improved(
    [0, 1, 2, 0, 2, 1, 1], 3) == [0, 0, 1, 2, 2, 1, 1])
assert(dutch_flag_partition_improved(
    [0, 1, 2, 0, 2, 1, 1], 1) == [0, 0, 1, 1, 1, 2, 2])
assert(dutch_flag_partition_improved(
    [0, 1, 2, 0, 2, 1, 1], 2) == [0, 1, 0, 1, 1, 2, 2])


# Time: O(n) | Space: O(1)
def dutch_flag_partition_alternative(array, pivot_index):
    pivot = array[pivot_index]

    # Keep the following invariants during partitioning:
    # botton group: A[:smaller].
    # middle group: A[smaller:equal].
    # unclassified group: A[equal:larger].
    # top group: A[larger:].
    smaller = 0
    equal = 0
    larger = len(array)

    # Keep iterating as long as there is an unclassified element.
    while equal < larger:
        # A[equal] is the incoming unclassified element.
        if array[equal] < pivot:
            array[smaller], array[equal] = array[equal], array[smaller]
            smaller += 1
            equal += 1
        elif array[equal] == pivot:
            equal += 1
        else:  # array[equal] > pivot
            larger -= 1
            array[equal], array[larger] = array[larger], array[equal]

    return array


assert(dutch_flag_partition_alternative(
    [0, 1, 2, 0, 2, 1, 1], 3) == [0, 0, 2, 2, 1, 1, 1])
assert(dutch_flag_partition_alternative(
    [0, 1, 2, 0, 2, 1, 1], 1) == [0, 0, 1, 1, 1, 2, 2])
assert(dutch_flag_partition_alternative(
    [0, 1, 2, 0, 2, 1, 1], 2) == [0, 1, 0, 1, 1, 2, 2])
