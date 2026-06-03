n,k=map(int,input().split())
count,highest=0,0
for _ in range(n):
    amount=int(input())
    if(amount>k):
        count+=1
    if(amount>highest):
        highest=amount
print("Violations:",count)
print("Highest Transaction:",highest)
    
