def array2str(array, reverse = False):
    result_string = "["
    if not reverse:
        for i in range(len(array) - 1):
            result_string += f"{str(array[i])}, "
        result_string += f"{str(array[-1])}]"
    else:
        for i in range(len(array) - 1, 0, -1):
            result_string += f"{array[i]}, "
    
        result_string += f"{str(array[0])}]"
    
    return result_string


numbers = [15, 8, 31, 47, 2, 19]

print(f"Existing array: {array2str(numbers)}")
print(f"Reversed array: {array2str(numbers, True)}")
