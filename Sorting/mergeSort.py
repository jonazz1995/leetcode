'''
Merge sort is a divide and conquer algorithm that divides the unsorted list into n 
sublists, each containing one element, and then repeatedly merges sublists to 
produce new sorted sublists until there is only one sublist remaining.
'''

def mergeSort(arr): # O(n log n) time complexity, O(n) space complexity
    if len(arr) <= 1:
        return arr
    
    # split the list in 2 halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    # Compare elements in the left and right sublists and merge them
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged


nums = [4,8,2,0,4,142,74625,85,6,2,4,8,88,52,2]
sorted_nums = mergeSort(nums)
print(sorted_nums)