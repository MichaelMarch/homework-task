import z10

def compare(array1, array2):
    len1 = len(array1)
    
    if not len1 == len(array2):
        return False

    for i in range(len1):
        if not array1[i] == array2[i]:
            return False
    
    return True

test_array = [
    ["water","book","sky"], ["water","book","sky"],
    [True, False], [True,False,True],
    [5,3,1], [5,3,1],
    [3,2,1], [3,2],
]

the_same_arrays = "The arrays are the same"
different_arrays = "The arrays are different"

for i in range(0, len(test_array), 2):
    print(f"Array1: {z10.array2str(test_array[i])}")
    print(f"Array2: {z10.array2str(test_array[i + 1])}")
    
    if compare(test_array[i], test_array[i + 1]):
        print(f"Comparison: {the_same_arrays}")
        continue
    
    print(f"Comparison: {different_arrays}")
        