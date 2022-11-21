import numpy as np

def binary_search(arr,l,r,x):
    if r>=l:
        mid=int(l+ (r-l)/2 )
        if arr[mid]==x:
            return mid
        if arr[mid]>x:
            return binary_search(arr,l,mid-1,x)
        else:
            return binary_search(arr,mid+1,r,x)
    else:
        return -1

arr = [ 2, 3, 4, 10, 40, 22,33,44,55,89] 
x=89

res=binary_search(arr,0,len(arr)-1,x)
print(res)