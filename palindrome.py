def palindrome(n):
    original = n
    reverse = 0
    while n !=0:
        last_digit = n % 10
        reverse = last_digit + reverse*10
        n//=10
    if original == reverse:
        return True
    else:
        False
if palindrome(121):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
