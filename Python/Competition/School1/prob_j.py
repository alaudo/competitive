import sys
sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[2], 'w')

import math
n, x, a = map(int, input().split())

one = a // x
total = math.ceil(n / one)
print(total)