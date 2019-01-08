def isarmstrong(n):
    s=0
    a=n
    while(n>0):
        r=n%10
        n=n//10
        s=s+r**3
    if(s==a):
        return True
    else:
        return False
a,b=map(int,input().split())
c=0
for i in range(a+1,b):
    if(isarmstrong(i)):
        if(c!=0):
            print(" ",end="")
        print(i,end="")
        c=c+1
