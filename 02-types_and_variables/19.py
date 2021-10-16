a = float(input("Enter side a = "))
b = float(input("Enter side b = "))
c = float(input("Enter side c = "))

semi_perimiter = (a + b + c) / 2

area = (semi_perimiter * (semi_perimiter - a) * (semi_perimiter - b) * (semi_perimiter - c)) ** 0.5

print(f"The area of a {a}, {b}, {c} trinagle is: {area}")