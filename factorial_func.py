def factorial_func(n):
    result = 1
    while n != 0:
        result *= n
        n-=1
    return result

print(factorial_func(5))