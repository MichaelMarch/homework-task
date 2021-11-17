counter = 0
with open("data/random_file_from_internet.txt", 'r') as file:
    for line in file:       
        if counter > 4:
            input("Press enter to show more")
            counter = 0

        print(line, end="")
        counter += 1