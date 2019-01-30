a,b=map(int,input().split())#input

for i in range(min(a,b),-1,-1):
    if(a%i==0 and b%i==0):
        print(i)
        break#break condition
