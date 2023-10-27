def binarySearch(arr, target):
    if len(arr) < 1:
        return False
    
    mid = len(arr) // 2

    if arr[mid] == target:
        return True
    
    elif arr[mid] < target:
        return binarySearch(arr[mid + 1:], target)
    else:
        return binarySearch(arr[:mid], target)


arr = [1,2,3,4,5,6,7]
print(binarySearch(arr, 10))