pln = int(input("Enter the amount in PLN: "))

amount_of_fives = pln // 5
amount_of_twos = (pln - (amount_of_fives * 5)) // 2
amount_of_ones = pln - (amount_of_twos * 2) - (amount_of_fives * 5)

print("The amount of PLN 18 in coins: ")
print(f"5 zł – {amount_of_fives}")
print(f"2 zł – {amount_of_twos}")
print(f"1 zł – {amount_of_ones}")