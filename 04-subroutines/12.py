def sum(N):
    return sum_helper(N)

def sum_helper(N, total_sum = 0):
    if N == 0:
        return total_sum
    else:
        return sum_helper(N - 1, total_sum + N)
    
print(f"{sum(10)}")
    