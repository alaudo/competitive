a = 5000
b = a
dividers = []
divisor = []
coprimes = []
 
for i in range(a-2):
    i = i+2
    dividers.append(int(i))
from math import sqrt
holder = 0
 
for i in range(2,int(a+1)):
    if (a % i) == 0:
        if not(i in divisor):
            divisor.append(int(i))

coprimes.append(int(1))
banned_numbers = []
already_used_number = []
for i in range(len(dividers)):
    for d in range(len(divisor)):
        yesorno = True
        if dividers[i] % divisor[d] == 0:
            banned_numbers.append(dividers[i])
            break
        else:
            for p in range(len(banned_numbers)):
                if dividers[i] == int(banned_numbers[p]):
                    yesorno = False
            for s in range(len(already_used_number)):
                if dividers[i] == int(already_used_number[s]):
                    yesorno = False
            if yesorno == True:
                already_used_number.append(dividers[i])
                coprimes.append(int(dividers[i]))
newlist = []
for i in range(len(coprimes)):
    if not(b % coprimes[i-1] == 0 and coprimes[i-1] != 1):
        newlist.append(coprimes[i-1])
print(len(newlist))