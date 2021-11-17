counter = 0

with open('data/countries.txt', 'r') as file:
    for line in file:
        counter += 1
        print(f"{counter} {line}", end="")
        