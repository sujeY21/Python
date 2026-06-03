C,S=map(int,input().split())
if(C>=750 and S>=50000):
    print("Approved")
elif(C>=650 and S>=30000):
    print("Review Required")
else:
    print("Rejected")
