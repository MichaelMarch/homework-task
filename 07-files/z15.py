file_path = input("Enter the name of the file: ")

line_counter = 0

with open(file_path, 'r') as file:
    for line in file:
        line_counter += 1

print(f"File name: {file_path}")
print(f"Number of lines: {line_counter}")