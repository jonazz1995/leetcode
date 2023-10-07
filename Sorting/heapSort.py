'''
Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to build a max-heap and 
then swaps the first element (maximum) with the last element (minimum) and finally calls heapify on the reduced heap.
'''

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] >  arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    

def heapSort(arr): # O(n log(n)) time complexity, O(1) space complexity
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap root with last element
        heapify(arr, i, 0)  # Re-heapify the reduced heap

nums = [4,8,2,0,4,142,74625,85,6,2,4,8,88,52,2]
heapSort(nums)
print(nums) 

'''using heapq'''
import heapq

def heapSortHeapq(arr):
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr

nums = [4,8,2,0,4,142,74625,85,6,2,4,8,88,52,2]
print(heapSortHeapq(nums))