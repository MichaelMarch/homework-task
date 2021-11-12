def is_subset(array1, array2):
    for element in array1:
        if not element in array2:
            return False
    
    return True