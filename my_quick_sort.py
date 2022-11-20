import numpy as np

def partition(arr,low,high):
    # i指示小于pivot的区间，j指使大于pivot的区间
    if low<high:
        i=low
        pivot=arr[high]
        for j in range(low,high):
            if arr[j]<pivot:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1

        arr[i],arr[high]=arr[high],arr[i]
        return i

def quickSort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)

        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

# arr = np.random.randint(low=0, high=20, size=(10))
arr=[10, 7, 2, 8, 9, 1, 5]
n=len(arr)
quickSort(arr,0,n-1)
print(arr)