n=int(input())
a=list(map(int,input().split()))
unique=[]
for i in a:
    if i not in unique:
        unique.append(i)
print(*unique)
