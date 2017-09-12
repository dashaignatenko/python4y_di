def fibonacci(n):
    x = 0
    y = 1
    for __ in range(n):
        x, y = y, (x + y)
    return x


print(fibonacci(int(input('n>>'))))
    
