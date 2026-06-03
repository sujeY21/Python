n=int(input())
a=list(map(int,input().split()))
natural_no=(n*(n+1)/2)
sum=0
for i in a:
    sum+=i
missing_no=natural_no-sum
print(int(missing_no))
