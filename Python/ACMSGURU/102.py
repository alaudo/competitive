# a = int(input())
from math import sqrt

# a = int(input())
a = 10000
b = a
dividers = []
    

while True:
    for i in range(2,b+1):
        if (b % i) == 0:
            if not(i in dividers):
                dividers.append(int(i))
            b = b // i
            break
    if  b == 1:
        break

allnums = list(range(a))
for d in dividers:
    allnums = list(filter(lambda x: x % d != 0, allnums))

print(len(allnums))

        