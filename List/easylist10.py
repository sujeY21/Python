n=int(input())
a=list(map(int,input().split()))
positive_count,negative_count,count=0,0,0
for i in a:
    if(i>0):
        positive_count+=1
    elif(i<0):
        negative_count+=1
    else:
        count+=1
print(positive_count,negative_count)




