array = [2, 3, 2, 5, 8, 1, 9, 8]

for i in range(len(array)):
    left = array[:i]
    right = array[i + 1:]
    if not array[i] in left and not array[i] in right:
        print(array[i], end=" ")
    