import re#import the re
s=str(input())
a=re.sub("\s\s+","",s)
print(a)
