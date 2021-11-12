def bubblesort(array):
    i = 0
    
    while i < len(array) - 1:
        j = 0
        while j < len(array) - i - 1:
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j += 1
        i += 1
    return array

#test_arrays = [
#    [3, 2, 1, 9, 2, 1, 7],
#    [19, 32, 100, 23, 51, 84, 21],
#    [-1, -10, -30, -2, -3, -9, -7],
#]
#for test_array in test_arrays:
#    print("-------------------------------------------")
#    print(f"Before: {test_array}")
#    bubblesort(test_array)
#    print(f"After: {test_array}")
#    print("-------------------------------------------")
#    print()