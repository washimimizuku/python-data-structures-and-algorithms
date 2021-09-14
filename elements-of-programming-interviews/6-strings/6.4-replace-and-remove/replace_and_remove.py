'''
Write a program which takes as input an array of characters,
and removes each 'b' and replaces each 'a' by two 'd's.
Specifically, along with the array, you are provided an
integer-valued size. Size denotes the number of entries of 
the array that the operation is to be applied to.
You do not have to worry about preserving subsequent entries.
For example, if the array is [a,b,a,c,...] and the size is 4,
then you can return [d,d,d,d,c].
You can assume there is enough space in the array to hold the
final result.
'''


def replace_and_remove(size, s):  # Time: O(n)
    # Forward iteration: remove 'b's and count the number of 'a's
    write_index, a_count = 0, 0

    for i in range(size):
        if s[i] != 'b':
            s[write_index] = s[i]
            write_index += 1
        if s[i] == 'a':
            a_count += 1

    # Backward iteration: replace 'a's with 'dd's starting from the end.
    current_index = write_index - 1
    write_index += a_count - 1
    final_size = write_index + 1

    while current_index >= 0:
        if s[current_index] == 'a':
            s[write_index - 1:write_index + 1] = 'dd'
            write_index -= 2
        else:
            s[write_index] = s[current_index]
            write_index -= 1
        current_index -= 1

    return (final_size, s)


assert(replace_and_remove(4, ['a', 'c', 'a', 'a', '', '', '']) == (
    7, ['d', 'd', 'c', 'd', 'd', 'd', 'd']))
