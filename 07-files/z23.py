import csv

with open("data/students.txt", 'r') as file:
    file.readline()
    
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
        