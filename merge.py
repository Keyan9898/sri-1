def mergeSort(li):
    if len(li)>1:
        mid = len(li)//2
        left = li[:mid]
        right = li[mid:]
        mergeSort(left)
        mergeSort(right)
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li[k]=left[i]
                i=i+1
            else:
                li[k]=right[j]
                j=j+1
            k=k+1
        while i < len(left):
            li[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            li[k]=right[j]
            j=j+1
            k=k+1
    print(li)
n=int(input())
li = list(map(int,input().split()))
mergeSort(li)
print(li)

