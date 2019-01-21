s=input()
count=0
c=["!","@","#","$","%","^","&","*","?","."]
for i in s:
    if(i in c):
        count=count+1
    
print(count)    
