import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"

temperatures = re.findall("\d{2}", message)

total_sum = 0
for temperature in temperatures:
    total_sum += int(temperature)

print(total_sum / len(temperatures))