weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

bmi = weight / (height / 100) ** 2

print(f"Your BMI index is equal to: {bmi}")
