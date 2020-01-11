import sys
sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[2], 'w')

import math
n = int(input())

if n % 2 == 0:
    print("Mahmoud")
else:
    print("Bashar")