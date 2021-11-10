def print_numpad():
    for i in range(3):
        for j in range(3):
            print(f"{3 * i + j + 1}", end = ' ')
        print()

print_numpad()