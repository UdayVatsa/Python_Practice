def fibonacci(n):
    term1,term2 = 1,1
    if n == 1:
        print(term1)
    print(term1)
    print(term2)
    for i in range(3,n+1):
        next_term = term1 + term2
        print(next_term)
        term1,term2 = term2,next_term
fibonacci(10)
