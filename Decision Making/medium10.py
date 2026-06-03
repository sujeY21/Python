L,D,S=map(int,input().split())
if(L>=8 and D>=2 and S>=1):
    print("Strong")
elif(L>=6 and D>=1):
    print("Medium")
else:
    print("Weak")
