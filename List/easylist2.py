n=int(input())
marks=list(map(int,input().split()))
marks.sort(reverse=True)
print(marks[0])
