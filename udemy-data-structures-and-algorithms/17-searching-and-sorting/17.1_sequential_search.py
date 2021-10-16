'''
Sequential search.
'''


def sequential_search(array, element):
    """
    General Sequential Search. Works on Unordered lists.
    """

    # Start at position 0
    position = 0
    # Target becomes True if element is in the list
    found = False

    # go until end of list
    while position < len(array) and not found:

        # If match
        if array[position] == element:
            found = True
        # Else move one down
        else:
            position += 1

    return found


arr = [7, 8, 2, 4, 9, 10, 1, 5, 6, 3]

assert(sequential_search(arr, 1) == True)
assert(sequential_search(arr, 3) == True)
assert(sequential_search(arr, 10) == True)

assert(sequential_search(arr, 100) == False)


def ordered_sequential_search(array, element):
    """
    Sequential search for an Ordered list
    """

    # Start at position 0
    position = 0
    # Target becomes true if ele is in the list
    found = False
    # Stop marker
    stopped = False

    # go until end of list
    while position < len(array) and not found and not stopped:

        # If match
        if array[position] == element:
            found = True
        else:
            # Check if element is greater
            if array[position] > element:
                stopped = True
            # Otherwise move on
            else:
                position += 1

    return found


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert(ordered_sequential_search(arr, 1) == True)
assert(ordered_sequential_search(arr, 3) == True)
assert(ordered_sequential_search(arr, 10) == True)

assert(ordered_sequential_search(arr, 100) == False)
