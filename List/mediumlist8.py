n=int(input())
a=list(map(int,input().split()))
for i in a:
    x=a.count(i)
    if(x>1):
        a.remove(i)
a.sort(reverse=True)
print(a[1])
            
    
