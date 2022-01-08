import re

text = "To be, or not to be, that is the question"

pattern = r"\b\w+"

matches = re.findall(pattern, text)

print(len(matches))

