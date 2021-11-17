with open("data/numbers_range.txt", 'w') as file:
    for i in range(1, 50 + 1):
        file.write(str(i) + '\n')