n=int(input())
a=list(map(int,input().split()))
k=int(input())
k=k%n
rest=a[:-k]
last=a[len(a)-k:len(a)]
rotated=rest+last
print(*rotated)



#n = int(input())
#a = list(map(int, input().split()))
#k = int(input())
#k = k % n
#rotated = a[-k:] + a[:-k]
#print(*rotated)
