n,d=map(int,input().split())
frequency=0
if(n==0 and d==0):
    count=1
else:
    while(n>0):
        digit=n%10
        if(digit==d):
            frequency+=1
        n//=10
print("Frequency:",frequency)
