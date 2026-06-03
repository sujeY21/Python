base,exp=map(int,input().split())
result=1
for i in range(exp):
    result=base*result
print(result)
