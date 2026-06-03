vehicle=input()
hours=int(input())
if(vehicle=="bike"):
    if(hours<=3):
        cost=20*hours
        print(cost)
    else: 
        cost=20*3+(hours-3)*10
        print(cost)
elif(vehicle=="car"):
    if(hours<=3):
        cost=50*hours
        print(cost)
    else:
        cost=50*3+(hours-3)*30
        print(cost)
else:
    print("Invalid Vehicle")
