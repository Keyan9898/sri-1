a=list(map(int,input().split())) #get the first input
b=list(map(int,input().split())) #get the second input
c=a[0]*60+a[1]
d=b[0]*60+b[1]
e=abs(c-d)
print(str(e//60)+" "+str(e%60))
