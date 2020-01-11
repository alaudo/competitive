import sys
sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[2], 'w')

import math
houses, gold = map(int,input().split())
amounts = list(map(int,input().split()))
mamount = -1

stepdata = []

for start in range(len(amounts)):
    cursum = amounts[start]
    end = start
    steps = 1
    while True:
        if cursum >= gold:
            break
        end += 1
        if end >= len(amounts):
            steps = -1
            break
        cursum += amounts[end]
        steps += 1
    if steps > 0:
        stepdata.append(steps)

if not(stepdata):
    print(-1)
else:
    print(min(stepdata))


