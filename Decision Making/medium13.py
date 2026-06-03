balance,amount=map(int,input().split())
pin=input()
if(pin=="invalid"):
    print("Invalid PIN")
elif(amount%100!=0):
    print("Invalid Amount")
elif(amount>balance):
    print("Insufficient Balance")
else:
    print("Transaction Successful")
