b,a=map(int,input().split())
s=list(map(int,input().split()))
d=sorted(s)
if(a in d):
    print("yes")
else:
    print("no")
