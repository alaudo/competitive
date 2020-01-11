a = input().strip().split()
b = input().strip().split()
c = input().strip().split()
dic = {}
di = {}
counter = 0
counter1 = 0
for i in b:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(len(dic)):
    d = int(a[1]) - int(dic[i])
    if d in dic and i != d:
        if dic[d] > dic[i]:
            counter += dic[i]
        else:
            counter += dic[d]
        del dic[d]
    del dic[i]
    

for i in c:
    if i in dic:
        di[i] += 1
    else:
        di[i] = 1
        
for i in di:
    d = a[1] - i
    if d in di and i != d:
        if di[d] > di[i]:
            counter1 += di[i]
        else:
            counter1 += di[d]
            del di[d]
        del di[d]
        
if counter == counter1:
    print("Tie")
elif counter > counter1:
    print("loser")
else:
    print("loser2")