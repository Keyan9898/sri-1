n=int(input())#input
v=1 
while(v<=n):
    if(n%v==0):
        print(format(v),end=" ")
    v=v+1
