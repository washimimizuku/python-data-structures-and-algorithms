def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(i + 1, length):
            if array[j] < array[i]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
bubble_sort(numbers)
print(numbers)
