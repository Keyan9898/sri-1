n=int(input())#input
if (n % 10):
    n = n + (10 - n % 10)
print(n)
