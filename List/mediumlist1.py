n=int(input())
a=list(map(int,input().split()))
compress=[]
for i in a:
    if(not compress or compress[-1]!=i):
        compress.append(i)
print(*compress)
    
