import math#import the math

n,a = map(int,input().split())
b=n*a
i = int(math.sqrt(b))
c=0
for s in range(n,a):
    if(b == i*i):
        c=c+1
print(c)
