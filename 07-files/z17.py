with open("data/random_file_from_internet.txt", 'r') as file:
    file_contents = file.read()
    
with open("data/copy.txt", 'w') as file:
    file.writelines(file_contents)