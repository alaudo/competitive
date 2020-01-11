import sys
sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[2], 'w')

import math
houses, gold = map(int,input().split())
amounts = list(map(int,input().split()))
t = len(amounts)

start, end = 0, 1
sizes = []

while True:
    s = sum(amounts[start:end])
    if s < gold:
        end += 1
        if end > t:
            break
    else:
        sizes.append((start, end, end-start))
        start += 1
        if end == start:
            end += 1
            if end > t:
                break

#print(sizes)

if sizes:
    print(min(map(lambda a:a[2],sizes)))
else:
    print(-1)

