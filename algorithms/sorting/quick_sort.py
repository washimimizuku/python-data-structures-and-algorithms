def quick_sort(array, left, right):
    if left < right:
        pivot = right
        partition_index = partition(array, pivot, left, right)

        quick_sort(array, left, partition_index - 1)
        quick_sort(array, partition_index + 1, right)

    return array


def partition(array, pivot, left, right):
    pivot_value = array[pivot]
    partition_index = left

    for i in range(left, right):
        if array[i] < pivot_value:
            swap(array, i, partition_index)
            partition_index += 1

    swap(array, right, partition_index)

    return partition_index


def swap(array, first_index, second_index):
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
sorted_numbers = quick_sort(numbers, 0, len(numbers) - 1)
print(sorted_numbers)
