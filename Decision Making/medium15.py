T=int(input())
cameraStatus=input()
if(cameraStatus=="off"):
    print("Block")
elif(T==0):
    print("Safe")
elif(T<=3):
    print("Warning")
else:
    print("Review Required")
