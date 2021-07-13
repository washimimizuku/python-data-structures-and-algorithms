def find_new_element_position(new_element, sorted_array):
    # Write your code here
    begin = 0
    end = len(sorted_array) - 1

    while begin < end:
        middle = round((end + begin) / 2)
        if new_element < sorted_array[middle]:
            end = middle - 1
        if new_element > sorted_array[middle]:
            begin = middle + 1

    if end == 0:
        return end
    else:
        return end + 1


assert(find_new_element_position(1, [2, 3, 4]) == 0)
assert(find_new_element_position(1, [2, 3, 4, 5]) == 0)

assert(find_new_element_position(6, [2, 3, 4]) == 3)
assert(find_new_element_position(6, [2, 3, 4, 5]) == 4)

assert(find_new_element_position(3, [1, 2, 4, 5]) == 2)
assert(find_new_element_position(10, [1, 2, 3, 4]) == 4)
assert(find_new_element_position(30, [10, 20]) == 2)
