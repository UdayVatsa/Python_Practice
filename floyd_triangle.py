def triangle(lines):
    num = 1
    for i in range(1,lines+1):
        for j in range(1,i+1):
            print(num,end = ' ')
            num+=1
        print()
lines = int(input("Enter the number of lines: "))
triangle(lines)