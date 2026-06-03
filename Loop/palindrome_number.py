n=int(input())
temp=n
rev=0
while(temp>0):
    digit=temp%10
    rev=rev*10+digit
    temp//=10
print("Reversed Number:",rev)
if(rev==n):
    print("Palindrome: Yes")
else:
    print("Palindrome: No")
    
