def armstrong(n):
    result = 0
    original = n
    while n != 0:
        last_digit = n%10
        term = pow(last_digit,3)
        result+=term
        n//=10
    if result == original:
        print("It is an armstrong number")
    else:
        print("It is not an armstrong number")

armstrong(153)