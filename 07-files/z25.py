import re

text = "To be, or not to be, that is the question"

pattern = r"e|u|i|o|a|y"

matches = re.findall(pattern, text)

print(len(matches))