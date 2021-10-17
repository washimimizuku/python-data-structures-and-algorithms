'''
Shell Sort

The shell sort improves on the insertion sort by breaking the
original list into a number of smaller sublists, each of which
is sorted using an insertion sort. The unique way that these
sublists are chosen is the key to the shell sort. Instead of
breaking the list into sublists of contiguous items, the shell
sort uses an increment i, sometimes called the gap, to create a
sublist by choosing all items that are i items apart.
'''


def shell_sort(array):  # Time: O((nlogn)2)
    sublist_count = len(array) // 2

    # While we still have sub lists
    while sublist_count > 0:
        for start in range(sublist_count):
            # Use a gap insertion
            gap_insertion_sort(array, start, sublist_count)

        sublist_count = sublist_count // 2


def gap_insertion_sort(array, start, gap):

    for i in range(start + gap, len(array), gap):

        # Set current values and position
        current = array[i]
        position = i

        # Using the Gap
        while position >= gap and array[position - gap] > current:

            array[position] = array[position - gap]
            position = position - gap

        # Set current value
        array[position] = current


arr = [3, 2, 13, 4, 6, 5, 7, 8, 1, 20]
shell_sort(arr)
assert(arr == [1, 2, 3, 4, 5, 6, 7, 8, 13, 20])
