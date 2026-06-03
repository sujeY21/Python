l,r=map(int,input().split())
count=0
for i in range(l,r+1):
    if(i>1):
        sum=0
        for j in range(1,i):
            if(i%j==0):
                sum+=j
        if (sum==i):
            count+=1
print("Perfect Number Count:",count)
