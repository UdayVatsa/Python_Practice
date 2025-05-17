import math

# Function to print prime number till n
def print_prime(n):
    if n >= 1:
        print(2)
    num = 3
    count = 1
    while count < n:
        for i in range(3,int(math.sqrt(num)) + 1,2):
            if num % i == 0:
                break
        else:
            count+=1
            print(num)
        num += 2
print_prime(5)
