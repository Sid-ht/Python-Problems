def binary_search(arr,low,high,x):

    if low <= high:
        mid = (low+high)//2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1


l = [4,5,6,7,18]
a = 7
low = 0
high = len(l)-1
result = binary_search(l,low,high,a)

if result == -1:
    print("element not found")
else:
    print("element found at index", str(result))
