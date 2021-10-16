'''
Sequential search.
'''


def sequential_search(array, element):

    position = 0
    found = False

    while position < len(array) and not found:

        if array[position] == element:
            found = True
        else:
            position += 1

    return found


arr = [7, 8, 2, 4, 9, 10, 1, 5, 6, 3]

assert(sequential_search(arr, 1) == True)
assert(sequential_search(arr, 3) == True)
assert(sequential_search(arr, 10) == True)

assert(sequential_search(arr, 100) == False)


def ordered_sequential_search(array, element):
    '''
    Input array must be sorted.
    '''

    position = 0
    found = False
    stopped = False

    while position < len(array) and not found and not stopped:

        if array[position] == element:
            found = True
        else:
            if array[position] > element:
                stopped = True
            else:
                position += 1

    return found


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert(ordered_sequential_search(arr, 1) == True)
assert(ordered_sequential_search(arr, 3) == True)
assert(ordered_sequential_search(arr, 10) == True)

assert(ordered_sequential_search(arr, 100) == False)
