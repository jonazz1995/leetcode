'''
Counting sort is a non-comparison-based sorting algorithm that works by counting 
the number of objects having distinct key values and then calculates the position of each object in the output sequence.
'''


def countingSort(arr): # O(n + k) where k is range of input and space complexity O(n)
    max_element = max(arr)

    # Create a count array to store the occurrences of each element
    count = [0] * (max_element + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

nums = [4,8,2,0,4,142,74625,85,6,2,4,8,88,52,2]
print(countingSort(nums))
