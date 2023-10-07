'''
Bucket Sort is a sorting algorithm that distributes the elements of an array into a number of buckets. 
Each bucket is then sorted individually, either using a different sorting algorithm or by recursively applying bucket sort. 
Finally, the sorted buckets are concatenated to get the sorted array.
mostly useful if array has uniform distribution of values, else most values will end up in one bucket
'''

def insertionSort(bucket):
    n = len(bucket)

    for i in range(1, n):
        key = bucket[i]
        j = i - 1

        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucketSort(arr): #O(n^2) in worst case, space is O(n+k)
    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]

    # Place elements into buckets
    for num in arr:
        index = int(num * num_buckets)
        buckets[index].append(num)

    # Sort individual buckets using insertion sort
    for bucket in buckets:
        insertionSort(bucket)

    # Concatenate sorted buckets to get the final sorted array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

nums = [46, 65, 12, 8, 51, 8, 23, 60, 83, 78, 4, 35, 7, 53, 42]
print(bucketSort(nums))

