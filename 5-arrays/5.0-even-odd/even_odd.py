'''
Given an array of integers, reorder its entries 
so that the even entries appear first.
'''


def even_odd(array):  # Time: O(2) | Space: O(1)
    next_even = 0
    next_odd = len(array) - 1

    while next_even < next_odd:
        if array[next_even] % 2 == 0:  # Is even
            next_even += 1
        else:
            array[next_even], array[next_odd] = array[next_odd], array[next_even]
            next_odd -= 1

    return array


assert(even_odd([1, 2, 3, 4, 5, 6])) == [6, 2, 4, 5, 3, 1]
