with open("data/random_file_from_internet.txt", 'r') as file:
    file_contents = file.read()
    
with open("data/copylines.txt", 'w') as file:
    for line in file_contents:
        file.write(line)