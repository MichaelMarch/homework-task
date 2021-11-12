numbers = [15, 8, 31, 47, 2, 19]

sum = 0

for i in range(len(numbers)):
    sum += numbers[i]

print(f"Arithmetic mean of numbers '{str(numbers)[1:-2]}' is {sum / len(numbers)}")
