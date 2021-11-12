import sys

def second_largest(array):
    largest_element = -sys.maxsize - 1
    second_largest_element = largest_element - 1
    
    
    for element in array:
        if element > largest_element:
            second_largest_element = largest_element
            largest_element = element
        elif element > second_largest_element:
            second_largest_element = element
            
    return second_largest_element
        
    
array = [5, 1, 9, 6, 1]


print(second_largest(array))