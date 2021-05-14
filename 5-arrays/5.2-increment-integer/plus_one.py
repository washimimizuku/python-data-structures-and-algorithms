'''
Write a program which takes as input an array of digits
encoding a nonnegative decimal integer D and updates the
array to represent the integer D + 1.
For example, if the input is (1,2,9) then you should
update the array to (1,3,0).
'''


def plus_one(array):  # Time: O(n), n = len(array)
    array[-1] += 1

    for i in reversed(range(1, len(array))):
        if array[i] != 10:
            break
        array[i] = 0
        array[i-1] += 1

    if array[0] == 10:
        # There is a carry-out, so we need one more digit
        # to store the result. A slick way to do this is
        # to append a 0 at the end of the array, and update
        # the first entry to 1.
        array[0] = 1
        array.append(0)
    return array


assert(plus_one([1, 2, 9]) == [1, 3, 0])
assert(plus_one([9, 9, 9]) == [1, 0, 0, 0])
assert(plus_one([0]) == [1])
