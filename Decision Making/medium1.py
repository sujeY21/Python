Income=int(input())
if(Income<=200000):
    print("No Tax Slab")
elif(Income>200000 and Income<=500000):
    print("Basic Slab")
elif(Income>500000 and Income<=750000):
    print("Standard Slab")
elif(Income>750000 and Income<=1000000):
    print("Higher Slab")
else:
    print("Premium Slab")
