import math
def is_prime(n):
    flag = True
    if n <= 1:
        flag = False
        return flag
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            flag = False
            break
    return flag

if (is_prime(1)):
    print("It is a prime number")
else:
    print("It is not prime")