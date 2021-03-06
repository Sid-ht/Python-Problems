def binary_search(arr,x):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] < x:
            low = mid +1
        elif arr[mid] > x:
            high = mid -1
        else:
            return mid
    return -1


l = [4,5,6,7,18]
a = 7
result = binary_search(l,a)

if result == -1:
    print("element not found")
else:
    print("element found at index", str(result))
