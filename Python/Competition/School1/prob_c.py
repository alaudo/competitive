import sys
sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[2], 'w')

x, y = map(int,input().split())

path = input()

for d in path:
    if d == 'U':
        y += 1
    elif d == 'D':
        y -= 1        
    elif d == 'L':
        x -= 1        
    elif d == 'R':
        x += 1   

    #print(d, x, y)                     

print(x,y)