import math#import the math

n,a = map(int,input().split())
c=0
for s in range(n,a):
    i = int(math.sqrt(s))
    if(s == i*i):
        c=c+1
print(c)
