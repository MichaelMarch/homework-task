import z18

def median(array):
    z18.bubblesort(array)
    length = len(array)
    if len(array) % 2 == 0:
        #size = 4
        # 1, 2
        # 4 / 2 - 1, 4 / 2
        return (array[length // 2 - 1] + array[length // 2]) / 2
    
    return array[length // 2]

tests = [
    [6, 8, 3, 1, 0, 5, 7],
    [1, 0, 9, 4, 6]
]

for test in tests:
    print(f"The median of {test} is: {median(test)}")
        
        