age=int(input())
day,seat=map(str,input().split())
if(day=="weekend"):
    if(seat=="premium"):
        if(age<12):
            print(250//2)
        else:
            print(250)
    elif(seat=="normal"):
        if(age<12):
            print(170//2)
        else:
            print(170)
    else:
        print("Invalid Seat")
else:
    if(seat=="premium"):
        if(age<12):
            print(200//2)
        else:
            print(200)
    elif(seat=="normal"):
        if(age<12):
            print(120//2)
        else:
            print(120)
    else:
        print("Invalid Seat")
    
        
    
