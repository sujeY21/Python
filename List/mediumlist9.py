n=int(input())
a=list(map(int,input().split()))
pivot=int(input())
b,c,d=[],[],[]
for i in a:
    if(i<pivot):
        b.append(i)
    elif(i>pivot):
        c.append(i)
    else:
        d.append(i)
b=b+d+c
print(*b)
