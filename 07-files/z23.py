import csv

with open("data/students.txt", 'r') as file:
    file.readline()
    
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if int(row[2]) < 30:
            print(f"{row[0]}\t{row[1]}\t{row[-1]}")