'''
Insertion sort builds the final sorted array one item at a time by 
repeatedly picking the next element from the unsorted part and inserting it into its correct position in the sorted part.
'''

def insertionSort(arr): # O(n^2) time complexity, O(1) space complexity
    n = len(arr)

    for i in range(1, n):
        key  = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


nums = [4,8,2,0,4,142,74625,85,6,2,4,8,88,52,2]
insertionSort(nums)
print(nums)