import sys
sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[2], 'w')

import math
import collections
n = int(input())

lst = input().split()
d = collections.Counter(lst)

total = 0

for k in d.values():
    total += 2 ** k - 1

print(int(total % (1E9 + 7) ))
