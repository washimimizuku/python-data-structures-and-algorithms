'''
Selection Sort

The selection sort improves on the bubble sort by making only
one exchange for every pass through the list. In order to do
this, a selection sort looks for the largest value as it makes
a pass and, after completing the pass, places it in the proper
location. As with a bubble sort, after the first pass, the
largest item is in the correct place. After the second pass, the
next largest is in place. This process continues and requires n−1
passes to sort n items, since the final item must be in place
after the (n−1) st pass.
'''


def selection_sort(array):  # Time: O(n2)

    # For every slot in array
    for fill_slot in range(len(array) - 1, 0, -1):
        position_of_max = 0

        # For every set of 0 to fill_slot + 1
        for location in range(1, fill_slot + 1):
            # Set maximum's location
            if array[location] > array[position_of_max]:
                position_of_max = location

        temp = array[fill_slot]
        array[fill_slot] = array[position_of_max]
        array[position_of_max] = temp


arr = [3, 2, 13, 4, 6, 5, 7, 8, 1, 20]
selection_sort(arr)
assert(arr == [1, 2, 3, 4, 5, 6, 7, 8, 13, 20])
