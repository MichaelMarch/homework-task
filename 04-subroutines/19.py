def power(x, n):
    return power_helper(x, n)    

def power_helper(x, n, accumulator = 1):
    if n == 0:
        return accumulator
    
    return power_helper(x, n - 1, accumulator * x)

print(f"{power_helper(2, 10)}")