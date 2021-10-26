total_sum = 0
count = 0

while True:
    num = int(input("Enter a number: "))
    
    if num == 0:
        break
    
    total_sum += num
    count += 1

print(f"RESULT: Quantity={count}, Sum={total_sum}, Mean={total_sum / count}")