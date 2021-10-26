a = 4
b = 15

print('*' * b)

for i in range(a - 2):
    print('*', end = '')
    
    for i in range(b - 2):
        print(end = ' ')
        
    print('*', end = '')
    print()

print('*' * b)