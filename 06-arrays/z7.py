numbers = [2, 9, 12312, 423, 123, 8173, 999, 2141, 2314]

even_counter = 0

for num in numbers:
    if num % 2 == 0:
        even_counter += 1
    
print(f"The number of even numbers is: {even_counter}")
print(f"The number of odd numbers is: {len(numbers) - even_counter}")