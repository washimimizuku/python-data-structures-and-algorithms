'''
Merge Sort

Merge sort is a recursive algorithm that continually splits a list
in half. If the list is empty or has one item, it is sorted by
definition (the base case). If the list has more than one item, we
split the list and recursively invoke a merge sort on both halves.
Once the two halves are sorted, the fundamental operation, called
a merge, is performed. Merging is the process of taking two smaller
sorted lists and combining them together into a single, sorted, new
list.
'''


def merge_sort(array):  # Time: O(nlogn)

    if len(array) > 1:

        # Split the list or sublist
        middle = len(array) // 2
        left_half = array[:middle]
        right_half = array[middle:]

        # Call merge sort on each half
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        # Sort list / sublist
        while i < len(left_half) and j < len(right_half):

            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1

            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1


arr = [3, 2, 13, 4, 6, 5, 7, 8, 1, 20]
merge_sort(arr)
assert(arr == [1, 2, 3, 4, 5, 6, 7, 8, 13, 20])
