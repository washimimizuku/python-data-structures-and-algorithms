'''
Binary search.
'''


def binary_search(array, element):

    first = 0
    last = len(array) - 1
    found = False

    while first <= last and not found:

        middle = (first + last) // 2

        if array[middle] == element:
            found = True
        else:
            if element < array[middle]:
                last = middle - 1
            else:
                first = middle + 1

    return found


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert(binary_search(arr, 1) == True)
assert(binary_search(arr, 3) == True)
assert(binary_search(arr, 10) == True)

assert(binary_search(arr, 100) == False)
