n=int(input())
a=list(map(int,input().split()))
p=0
for i in range(n):
    for j in range(i+1,n):
        if(a[j]>a[i]):
            b=a[j]-a[i]
            if(b>p):
                p=b
print(p)
    
