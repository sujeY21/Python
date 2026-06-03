n=int(input())
a=list(map(int,input().split()))
leaders=[]
for i in range(n):
    is_leader=True
    for j in range(i+1,n):
        if(a[j]>a[i]):
            is_leader=False
            break
    if(is_leader):
        leaders.append(a[i])
print(*leaders)
