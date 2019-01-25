n=input()#input
a=len(n)//2#middle of string
c=list(n)
for i in range(len(c)):
    if(len(n)%2==0):
        c[a-1],c[a]="*","*"
    else:
        c[a]="*"
for i in c:
    print(i,end="")
