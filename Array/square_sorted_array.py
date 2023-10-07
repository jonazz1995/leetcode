'''
function to output a sorted array of squared values, from a sorted array
[-2, -1, 1, 3, 5] -> [1, 1, 4, 9, 25]
'''

def squared_sorted_array(arr):
    res = []
    l, r = 0, len(arr) - 1

    while l <= r:
        if abs(arr[l]) > abs(arr[r]):
            res.append(arr[l]**2)
            l += 1
        else:
            res.append(arr[r]**2)
            r -= 1

    return res[::-1]

arr = [-2, -1, 1, 3, 5]

print(squared_sorted_array(arr))