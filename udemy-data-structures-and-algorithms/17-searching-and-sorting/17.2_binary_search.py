'''
Binary search.
'''


def binary_search(array, element):

    # First and last index values
    first = 0
    last = len(array) - 1

    found = False

    while first <= last and not found:

        middle = (first + last) // 2

        # Match found
        if array[middle] == element:
            found = True
        else:
            # Set new midpoints up or down depending on comparison
            if element < array[middle]:
                # Set down
                last = middle - 1
            # Set up
            else:
                first = middle + 1

    return found


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert(binary_search(arr, 1) == True)
assert(binary_search(arr, 3) == True)
assert(binary_search(arr, 10) == True)

assert(binary_search(arr, 100) == False)


def binary_search_recursive(array, element):

    # Base Case!
    if len(array) == 0:
        return False

    # Recursive Case
    else:
        middle = len(array) // 2

        # If match found
        if array[middle] == element:
            return True

        else:

            # Call again on second half
            if element < array[middle]:
                return binary_search_recursive(array[:middle], element)

            # Or call on first half
            else:
                return binary_search_recursive(array[middle + 1:], element)


arr = [1, 2, 3, 4, 5]

assert(binary_search_recursive(arr, 1) == True)
assert(binary_search_recursive(arr, 3) == True)
assert(binary_search_recursive(arr, 5) == True)

assert(binary_search_recursive(arr, 100) == False)
