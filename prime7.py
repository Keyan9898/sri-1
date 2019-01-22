n=int(input()) #get the input
if(n>1):
    for i in range(2,n):#for loop
        if(n%i==0):
            print("no")
            break#condition
    else:
        print("yes")
else:
    print("no")
