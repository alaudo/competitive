a = int(input())
dividers = []
divisor = []
coprimes = []
#for i in range(a):
    #while True:
        #if (a % i) == 0 and a >= i:
            #dividers.append(a/i)
        #else:
            #break
for i in range(a-2):
    i = i+2
    dividers.append(i)
from math import sqrt
while True:
    for i in range(2,int(sqrt(a)+1)):
        if (a % i) == 0:
            a = a//i
            if not(i in divisor):
                divisor.append(i)
            break
    if a == 1:
        break
for d in range(len(divisor)):
    if dividers[i] % divisor[d] == 0:
        break
    else:
        coprimes.append(dividers[i])
print(len(coprimes))
        