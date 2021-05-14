'''
Write a program which takes as input a sorted array
and updates it so that all duplicates have been removed
and the remaining elements have been shifted left to
fill the emptied indices.
Return the number of valid elements.
'''


def delete_duplicates(array):  # Time: O(n) | Space: O(1)
    if not array:
        return 0

    write_index = 1
    for i in range(1, len(array)):
        if array[write_index - 1] != array[i]:
            array[write_index] = array[i]
            write_index += 1
    return write_index


assert(delete_duplicates([]) == 0)
assert(delete_duplicates([1, 1, 1]) == 1)
assert(delete_duplicates([1, 2, 3]) == 3)
assert(delete_duplicates([2, 3, 5, 5, 7, 11, 11, 11, 13]) == 6)
