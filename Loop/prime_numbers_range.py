l,r=map(int,input().split())
count=0
for i in range(l,r+1):
    if(i>1):
        is_prime=True
        for j in range(2,i):
            if(i%j==0):
                is_prime=False
                break
        if (is_prime):
            count+=1
print("Prime Count:",count)
