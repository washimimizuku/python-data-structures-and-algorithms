'''
Write a program that takes an array A of n numbers,
and rearranges A's elements to get a new array B
having the property that:
 B[0] < B[1] > B[2] < B[3] > B[4] < B[5] > ...
'''


def rearrange(array):  # Time: O(n)
    for i in range(len(array) - 1):
        if ((i % 2 and array[i] < array[i + 1]) or
                (not i % 2 and array[i] > array[i + 1])):
            array[i], array[i + 1] = array[i + 1], array[i]

    return array


assert(rearrange([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 2, 5, 4, 7, 6, 9, 8])
assert(rearrange([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [8, 9, 6, 7, 4, 5, 2, 3, 1])
assert(rearrange([12, 11, 13, 9, 12, 8, 14, 13, 15])
       == [11, 13, 9, 12, 8, 14, 12, 15, 13])
assert(rearrange([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])
       == [310, 315, 275, 295, 260, 290, 230, 270, 250, 255])


def rearrange_with_sorted(array):  # Time: O(n)
    for i in range(len(array)):
        array[i: i + 2] = sorted(array[i:i + 2], reverse=i % 2)

    return array


assert(rearrange_with_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9])
       == [1, 3, 2, 5, 4, 7, 6, 9, 8])
assert(rearrange_with_sorted([9, 8, 7, 6, 5, 4, 3, 2, 1])
       == [8, 9, 6, 7, 4, 5, 2, 3, 1])
assert(rearrange_with_sorted([12, 11, 13, 9, 12, 8, 14, 13, 15])
       == [11, 13, 9, 12, 8, 14, 12, 15, 13])
assert(rearrange_with_sorted([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])
       == [310, 315, 275, 295, 260, 290, 230, 270, 250, 255])
