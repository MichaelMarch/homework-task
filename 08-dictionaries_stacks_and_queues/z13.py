import json

with open("data/random_file_from_the_internet.json") as file:
    data = json.load(file)

for k,v in data.items():
    print(k,":",v)
