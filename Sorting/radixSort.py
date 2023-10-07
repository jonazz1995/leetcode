'''
Radix Sort is a non-comparison-based sorting algorithm that works by distributing elements into 
buckets according to their digits, from the least significant digit (LSD) to the most significant digit (MSD), 
and then collecting them back into a single array. Radix Sort can be implemented using counting sort as a subroutine 
for each digit position.
'''

def countingSort(arr, exp): # O(n * k) where k is range of input and space complexity O(n)
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit at the specified exponent
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Update count array to store actual positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array using the positions from count array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array back to the original array
    for i in range(n):
        arr[i] = output[i]

def radixSort(arr):
    max_element = max(arr)

    # Do counting sort for each digit position, from LSD to MSD
    exp = 1
    while max_element // exp > 0:
        countingSort(arr, exp)
        exp *= 10

nums = [4,8,2,0,4,142,74625,85,6,2,4,8,88,52,2]
radixSort(nums)
print(nums)