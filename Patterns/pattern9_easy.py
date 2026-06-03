n=int(input())
a,b=0,1
print(a,b,end=" ")
for i in range(n-2):
    sum=a+b
    a=b
    b=sum
    print(sum,end=" ")
    
    
    
    
