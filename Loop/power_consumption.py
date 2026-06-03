n=int(input())
low_count=0
normal_count=0
high_count=0
for i in range(n):
    units=int(input())
    if(units<100):
        low_count+=1
    elif(100<=units<=300):
        normal_count+=1
    else:
        high_count+=1
print("Low:",low_count,"\nNormal:",normal_count,"\nHigh:",high_count)
