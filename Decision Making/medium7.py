amount,distance=map(int,input().split())
if(amount>=1000):
    print("Free Delivery")
elif(distance<=5):
    print(40)
elif(distance<=10 and distance>5):
    print(70)
else:
    print(120)
