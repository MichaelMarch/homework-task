numbers1 = [4, 36, 12, 28, 9, 44, 5]
numbers2 = [5, 1, 36]

for number in numbers1:
    if not number in numbers2:
        print(number, end=" ")