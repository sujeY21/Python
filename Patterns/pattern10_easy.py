n=int(input())
count=0
number=2
while(count<n):
    for i in range(2,number):
        if(number%i==0):
            break
    else:
        print(number,end=" ")
        count+=1
    number+=1
    
    
