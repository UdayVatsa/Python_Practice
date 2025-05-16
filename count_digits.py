def count_dig(n):
    count = 0
    if n==0:
        return 1
    while n!=0:
        count+=1
        n//=10
    return count

ans = count_dig(437)
print(ans)