def binary_search(arr, target):
    if not arr:
        return False
    
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left+right)//2

        if arr[mid] == target:
            return True

        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False        

numbers = [1,2,3,4,5]
print(binary_search(numbers, 6))