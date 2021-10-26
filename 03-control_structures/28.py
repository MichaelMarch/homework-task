def fib(x, left = 0, right = 1):
    if x == 0:
        return
    else:
        print(left)
        fib(x - 1, right, left + right)
        
fib(50)