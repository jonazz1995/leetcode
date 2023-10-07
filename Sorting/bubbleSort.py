'''
 Bubble sort is a simple sorting algorithm that repeatedly steps through the list, 
 compares adjacent elements, and swaps them if they are in the wrong order.
 '''

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        
nums = [4,8,2,0,4,142,74625,85,6,2,4,8,88,52,2]
bubbleSort(nums)
print(nums)