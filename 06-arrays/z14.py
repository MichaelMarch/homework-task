names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest_name_index = 0

for i in range(1, len(names)):
    if len(names[longest_name_index]) >= len(names[i]):
        continue
    
    longest_name_index = i

print(f"Names: {names}")
print(f"Longest name: {names[longest_name_index]}")