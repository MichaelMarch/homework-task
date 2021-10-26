x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    x, y = y, x

print(f"Numbers in ascending order: {x}, {y}")