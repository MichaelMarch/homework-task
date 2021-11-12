def array2str(array):
    return str(array)[1:-1]

test = [5,4,3,2,6,5]
print(f"Array: {test}")
print(f"Result: {array2str(test)}")