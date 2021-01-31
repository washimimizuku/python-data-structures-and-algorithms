def selection_sort(array):
    length = len(array)

    for i in range(length):
        minimum = array[i]
        index = i
        for j in range(i + 1, length):
            if array[j] < minimum:
                index = j
                minimum = array[j]
        array[i], array[index] = array[index], array[i]
    
    return array



numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)