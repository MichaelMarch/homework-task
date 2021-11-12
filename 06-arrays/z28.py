array = [1, 23, 5, 382, 1, 17, 4, 906]

seperator = ""
middle_section = ""


for element in array:
    seperator += ("-" * 5)
    middle_section += f"|{str(element).rjust(4)}"

seperator += "-"

middle_section += "|"

print(seperator)
print(middle_section)
print(seperator)
    
    
    
