s=input()
count=0
c=["!","@","#","$","%","^","&","*","?",".","_"]
for i in s:
    if(i in c):
        count=count+1
    
print(count)    
