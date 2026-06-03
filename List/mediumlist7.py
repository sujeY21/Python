n=int(input())
a=list(map(int,input().split()))
zeros=[]
result=[]
for i in a:
    if(i==0):
        zeros.append(i)
    else:
        result.append(i)
result=result+zeros
#result.extend(zeros)
print(*result)
        
