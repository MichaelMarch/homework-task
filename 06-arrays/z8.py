import sys

numbers = [-15, 8, -31, 47, -2, 19]


min_value = sys.maxsize
max_value = -min_value - 1

for i in numbers:
    if i < min_value:
        min_value = i
    if i > max_value:
        max_value = i

print(f"Max number is: {max_value}")
print(f"Min number is: {min_value}")