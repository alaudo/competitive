import sys
sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[2], 'w')

import math
n, k = map(int,input().split())
mahmoud = list(map(int,input().split()))
bashar = list(map(int,input().split()))

def make_count(lst):
    d = {}
    for l in lst:
        if l in d:
            d[l] += 1
        else:
            d[l] = 1
    return d

def countpairs(ls, num):
    l = make_count(ls)
    counter = 0
    for k in l.keys():
        if (num - k) in l:
            counter += l[k] * l[(num-k)]
    return counter

m = countpairs(mahmoud,k)
b = countpairs(bashar,k)

if m > b:
    print("Mahmoud")
elif m < b:
    print("Bashar")
else:
    print("Draw")
