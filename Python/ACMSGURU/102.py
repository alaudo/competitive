from math import sqrt


def allmultipule(a):
    multipule = []
    a = int(a)
    for i in range(1,int(sqrt(a))+1):
        i = int(i)
        if a % i == 0:
            multipule.append(i)

    for s in range(len(multipule)):
        if a % multipule[s] == 0 and a // multipule[s] != multipule[s]:
            multipule.append(a//multipule[s])
    return sorted(multipule)

def GCD(a,b):
    a = allmultipule(a)
    print(a)
    b = allmultipule(b)
    print(b)
    c = set(a).intersection(b)
    return max(c)

def lcm(a,b):
        return a * b // GCD(a,b)

print(GCD(15,24))
print(lcm(24,15))