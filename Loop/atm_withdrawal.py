n=int(input())
valid_count=0
invalid_count=0
total_amount=0
for _ in range(n):
    amount=int(input())
    if(amount>0 and amount%100==0):
        valid_count+=1
        total_amount+=amount
    else:
        invalid_count+=1
print("Valid Requests:",valid_count)
print("Invalid Requests:",invalid_count)
print("Total Amount",total_amount)
