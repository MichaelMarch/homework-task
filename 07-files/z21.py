with open("data/3-digit_numbers_range.txt", 'w') as file:
    for i in range(100, 999 + 1):
        file.write(str(i) + '\n')