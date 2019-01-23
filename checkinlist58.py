a,b=map(int,input().split())#get list size and check element

s=list(map(int,input().split()))
c=0
for i in range(0,len(s)):
    if(s[i]==b):
        c=c+1 
if(c>0):
    print("yes")
else:
    print("no")
