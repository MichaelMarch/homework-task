def group_by_parity(array):
    l = 0
    r = len(array) - 1
    while l < r:
        if not array[l] % 2 == 0 and array[r] % 2 == 0:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1
        else:
            if array[l] % 2 == 0:
                l += 1
            if not array[r] % 2 == 0:
                r -= 1
                
test = [9, 1, 3, 2, 8, 7, 0, 4, 6, 5]            
group_by_parity(test)

print(test)
