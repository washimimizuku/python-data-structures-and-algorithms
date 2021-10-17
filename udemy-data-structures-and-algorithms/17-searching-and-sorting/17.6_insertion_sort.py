'''
Insertion Sort

Insertion Sort builds the final sorted array (or list) one item
at a time. It is much less efficient on large lists than more
advanced algorithms such as quicksort, heapsort, or merge sort.
'''


def insertion_sort(array):  # Time: O(n2)

    # For every index in array
    for i in range(1, len(array)):

        # Set current values and position
        current = array[i]
        position = i

        # Sorted sublist
        while position > 0 and array[position - 1] > current:

            array[position] = array[position - 1]
            position = position - 1

        array[position] = current


arr = [3, 2, 13, 4, 6, 5, 7, 8, 1, 20]
insertion_sort(arr)
assert(arr == [1, 2, 3, 4, 5, 6, 7, 8, 13, 20])
