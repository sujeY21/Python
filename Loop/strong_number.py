n=int(input())
n1=n
sum=0
while(n1>0):
    digit=n1%10
    n1//=10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum+=fact
if(sum==n):
    print("Strong Number:Yes")
else:
    print("Strong Number:No")
    
