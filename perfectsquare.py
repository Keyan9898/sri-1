import math#import the math

n,a = map(int,input().split())
b=n*a
i = int(math.sqrt(b))

if(b == i*i):
  print("yes")
else:
  print("no")
