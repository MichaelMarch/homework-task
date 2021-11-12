def sum(array):
    total_sum = 0
    
    for i in array:
        total_sum += i
    
    return total_sum

def array2str(array):
    result_string = ""
    
    for i in array:
        result_string += f"{i} "
    
    return result_string

test_array = [4, 3, 7, 1, 3]

print(array2str(test_array))
print(sum(test_array))
