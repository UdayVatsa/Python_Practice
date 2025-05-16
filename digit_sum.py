def dig_sum(n):
    result = 0
    while n != 0:
        last_digit = n % 10
        result+=last_digit
        n //=10
    return result

ans = dig_sum(367)
print(ans)