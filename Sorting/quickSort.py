'''
Quick sort is also a divide and conquer algorithm that works by selecting a 
'pivot' element from the array and partitioning the other elements into two sub-arrays, 
according to whether they are less than or greater than the pivot.

selection pivot in cruicial - can do first or last element but not efficient if already partially sorted
can select random pivot
or can do median of three (left, middle and right) - best in practice
'''

def quickSort(arr): # O(n log n) time complexity, O(n) space complexity
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left, right, middle = [], [], []

    # Partition the elements into left, middle, and right sublists
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            middle.append(num)
        else:
            right.append(num)
        
    return quickSort(left) + middle + quickSort(right)

nums = [4,8,2,0,4,142,74625,85,6,2,4,8,88,52,2]
sorted_nums = quickSort(nums)
print(sorted_nums)  