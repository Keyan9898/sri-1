import collections#import the collection
n=input()
l=list(map(int,input().split()))#get the list
f=collections.Counter(l)
for x,y in f.items():
    if(y<=1):
        print(x)
