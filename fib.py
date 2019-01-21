s=int(input())#input
a=1 
b=1 
c=0
d=0
print(a,b,end=" ")
for i in range(2,s):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
if(d!=0):#space removal at end
    print(" ",c)
 else:
    print("")
