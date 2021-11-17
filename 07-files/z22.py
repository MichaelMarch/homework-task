with open("data/powers.txt", 'w') as file:
    for i in range(1, 10 + 1):
        file.write(f"{i},{pow(i, 2)},{pow(i, 3)}\n")