import sys
sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[2], 'w')

a = int(input())
print(2 * a)

