'''
Given an array A of n elements and a permutation P,
apply P to A.
For example, the permutation [2, 0, 1, 3] applied to 
A = [a, b, c, d] yields the array [b, c, a, d].
'''


def apply_permutation(array, permutation):  # Time: O(n) | Space: O(1)
    for i in range(len(array)):
        # Check if the element at index i has not been
        # moved by checking if pern[i] is non-negative.
        next_element = i
        while permutation[next_element] >= 0:
            array[i], array[permutation[next_element]
                            ] = array[permutation[next_element]], array[i]
            temp = permutation[next_element]

            # Subtracts len(permutation) fron an entry
            # in permutation to make it negative, which
            # indicates the corresponding move has been
            # performed.
            permutation[next_element] -= len(permutation)
            next_element = temp

    # Restore permutation
    permutation[:] = [a + len(permutation) for a in permutation]

    return array


assert(apply_permutation(['a', 'b', 'c', 'd'],
       [2, 0, 1, 3]) == ['b', 'c', 'a', 'd'])


# Time: O(n2) | Space: O(1)
def apply_permutation_no_negative(array, permutation):
    def cyclic_permutation(start, permutation, array):
        i = start
        temp = array[start]
        while True:
            next_i = permutation[i]
            next_temp = array[next_i]
            array[next_i] = temp
            i, temp = next_i, next_temp
            if i == start:
                break

    for i in range(len(array)):
        # Traverses the cycle to see if i is the
        # minimum elenent.
        j = permutation[i]
        while j != i:
            if j < i:
                break
            j = permutation[j]
        else:
            cyclic_permutation(i, permutation, array)

    return array


assert(apply_permutation_no_negative(['a', 'b', 'c', 'd'],
       [2, 0, 1, 3]) == ['b', 'c', 'a', 'd'])
