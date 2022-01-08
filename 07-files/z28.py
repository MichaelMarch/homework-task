import re
with open("data/grades.txt") as file:
    file.readline()
    line = file.readline()
    
    pattern = r"[0-5]\.[05]"
    
    matches = re.findall(pattern, line)
    
    total_sum = 0.0
    for match in matches:
        total_sum += float(match)
        
    print(total_sum / len(matches))
    