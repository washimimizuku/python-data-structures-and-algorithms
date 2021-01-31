def insertion_sort(array):
    length = len(array)
    for i in range(length):
        if array[i] < array[0]:
            temp = array[i]
            array.pop(i)
            array.insert(0,temp)
        else:
            if array[i] < array[i-1]:
                for j in range(1, i):
                    if (array[i] >= array[j-1]) and (array[i] < array[j]):
                        temp = array[j]
                        array[j] = array[i]
                        array[i] = temp



numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
insertion_sort(numbers)
print(numbers)