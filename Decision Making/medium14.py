amount=int(input())
userType=input()
if(userType=="new" and amount>=299):
    print("Extra 2GB")
elif(userType=="existing" and amount>=499):
    print("Cashback 50")
elif(amount<100):
    print("Invalid Recharge")
else:
    print("Standard Benefits")
