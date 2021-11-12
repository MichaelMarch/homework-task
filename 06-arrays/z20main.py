import z19

array = [15, 38, 7, 23, 14]

number = int(input("Enter a number: "))

if z19.occurs(number, array):
    print(f"Number: {number} is present in the array")
else:
    print(f"Number: {number} is not present in the array")
