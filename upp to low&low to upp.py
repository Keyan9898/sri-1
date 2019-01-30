s=str(input())#get the input
for i in s:
    if(i.islower()):
        a=i.upper()
    elif(i.isupper()):
        a=i.lower()
    print(a,end="")#output
