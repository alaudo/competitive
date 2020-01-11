import sys
sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[2], 'w')

a = int(input())
div = 1

for div in range(2,a+1):
    if a % div == 0:
        break

print(div, a // div)