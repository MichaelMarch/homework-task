def is_prime(x):
    if x < 2:
        return false
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True

N = int(input("Enter a number: "))

print("Prime numbers: ", end = '')
for i in range(2, N + 1):
    if is_prime(i):
        print(i, end = ' ')

