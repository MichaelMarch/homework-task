array = [.3, 1.4, 23.1, 72.923, 12.124, 42.001, 100.24, 329.27]

threshold = float(input("Enter a number: "))

counter = 0

for element in array:
    if element > threshold:
        counter += 1

print(f"There is {counter} number of elements greater than {threshold}")
