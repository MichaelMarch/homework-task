def power(x, n):
    if n == 0:
        return x
    
    return power(x * x, n - 1)

print(f"{power_helper(2, 10)}")