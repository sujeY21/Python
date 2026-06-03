n=int(input())
a=list(map(int,input().split()))
last=a[-1]
rest=a[0:-1]
rotated=[last]+rest
print(*rotated)
