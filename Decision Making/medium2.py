P,I=map(int,input().split())
if(P>=90 and I<=200000):
    print("Full Scholarship")
elif(P>=80 and P<=400000):
    print("Half Scholarship")
else:
    print("Not Eligible")
