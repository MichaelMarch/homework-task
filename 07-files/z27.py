import re



with open("data/random_file_from_internet.txt") as file:
    file_contents = file.read()
    matches = re.findall(r"\w{6,}", file_contents)
    print(len(matches))
    