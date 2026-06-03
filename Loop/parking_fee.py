n,k=map(int,input().split())
count=0
sum=0
for _ in range(n):
    fee=int(input())
    if(fee>k):
        count+=1
    sum+=fee
print("Total Collection:",sum)
print("Above Expexted:",count)
