s,inc,t=map(int,input().split())
days=0
total_amount=0
while(total_amount<t):
    total_amount+=s
    days+=1
    s+=inc
print("Days Required:",days)
