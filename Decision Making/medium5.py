A,B,C=map(int,input().split())
if((A+B>C) and (A+C>B) and (B+C>A)):
    if(A==B==C):
        print("Equilateral")
    elif(A==B or B==C or A==C):
        print("Isoceles")
    else:
        print("Scalene")
else:
    print("Invalid Triangle")
