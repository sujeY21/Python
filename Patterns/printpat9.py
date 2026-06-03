n=int(input())
for i in range(1,n+1):
    star=2*i-1
    print(" "*(n-i),"*"*star)
for i in range(n-1,0,-1):
    star=2*i-1
    print(" "*(n-i),"*"*star)

