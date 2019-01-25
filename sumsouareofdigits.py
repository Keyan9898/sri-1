n=int(input())#input
su=0
r=2
while(n>0):
    num=n%10
    su=su+num**r#sum of square of its digits
    n=n//10
print(su)
