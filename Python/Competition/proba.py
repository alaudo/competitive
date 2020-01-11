import sys
from io import StringIO

oldstdin = sys.stdin

sys.stdin = open(sys.argv[1], 'r')
sys.stdin = open(sys.argv[2], 'w')

a = input()

print(sys.argv)
print(a)