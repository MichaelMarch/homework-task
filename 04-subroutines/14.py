weight = int(input("Enter the weight in kg: "))
height = int(input("Enter the height in m: "))

bmi_formula = lambda w, h: w / (h / 100) ** 2

print(f"BMI is equal to: {bmi_formula(weight, height)}")