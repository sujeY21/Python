exp=int(input())
rating=float(input())
if(exp>=5 and rating>=4.5):
    print("20% Bonus")
elif(exp>=3 and rating>=4.0):
    print("10% Bonus")
elif(rating<3.0):
    print("No Bonus")
else:
    print("5% Bonus")



    
