'''
Quick Sort
A quick sort first selects a value, which is called the pivot value.
Although there are many different ways to choose the pivot value, we
will simply use the first item in the list. The role of the pivot
value is to assist with splitting the list. The actual position where
the pivot value belongs in the final sorted list, commonly called the
split point, will be used to divide the list for subsequent calls to
the quick sort.
'''


def quick_sort(array):  # Time: O(nlogn)

    quick_sort_help(array, 0, len(array) - 1)


def quick_sort_help(array, first, last):

    if first < last:
        split_point = partition(array, first, last)
        quick_sort_help(array, first, split_point)
        quick_sort_help(array, split_point + 1, last)


def partition(array, first, last):

    pivot_value = array[first]

    left_mark = first + 1
    right_mark = last

    done = False

    while not done:

        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark += 1

        while arr[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True

        else:
            temp = array[left_mark]
            array[left_mark] = array[right_mark]
            array[right_mark] = temp

    temp = array[first]
    array[first] = array[right_mark]
    array[right_mark] = temp

    return right_mark


arr = [3, 2, 13, 4, 6, 5, 7, 8, 1, 20]
quick_sort(arr)
assert(arr == [1, 2, 3, 4, 5, 6, 7, 8, 13, 20])
