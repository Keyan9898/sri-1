import numpy
n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
print(numpy.median(b))
