'''
Selection sort sorts an array by repeatedly finding the minimum 
element from the unsorted part of the array and putting it at the beginning.
'''

def selectionSort(arr): # O(n^2) time complexity, O(1) space complexity
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1,n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i] 


        
nums = [4,8,2,0,4,142,74625,85,6,2,4,8,88,52,2]
selectionSort(nums)
print(nums)