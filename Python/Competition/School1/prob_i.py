import sys
sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[2], 'w')

import math
n = int(input())
lst = input()

d = {}
for l in lst:
    if l in d:
        d[l] += 1
    else:
        d[l] = 1

minnum = min(d.values()) if len(d) == 5 else 0
maxnum = max(d.values()) if len(d) > 0 else 0

print(minnum, maxnum)

