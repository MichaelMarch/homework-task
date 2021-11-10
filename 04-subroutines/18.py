def sum_digits(x):
    total_sum = 0
    
    while x != 0:
        total_sum += int(x % 10)    
        x /= 10
        
    return total_sum

print(f"{sum_digits(7182)}")
