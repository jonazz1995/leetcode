'''
array of integers arr = [1,5,2,3,7,1], k=3 
[2,3,7] = 12
sliding window two pointers slide one along until second pointer out of bounds
         l   r
[1,5,2,3,7,1] , len = 6 
'''

def k_consecutive_elements(arr, k):
    l, r = 0, k
    max_sum = 0

    while r < len(arr):
        max_sum = max(max_sum, sum(arr[l:r]))
        l += 1
        r += 1
    return max_sum


arr = [5, -3, 7, -6, 8]
print(k_consecutive_elements(arr, 3))

