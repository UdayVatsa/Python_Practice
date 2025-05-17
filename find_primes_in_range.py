import math

n = 3 #range
if n > 1:
    print(2)
for i in range(3,n+1,2):
    for j in range(3,int(math.sqrt(i)+1),2):
        if i%j == 0:
            break
    else:
        print(i)