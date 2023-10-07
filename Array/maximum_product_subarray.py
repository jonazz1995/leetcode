def maxProduct(nums):
        res = max(nums)
        maxSum, minSum = 1, 1

        for num in nums:
            tmp = num * maxSum
            maxSum = max(num, maxSum * num, minSum * num)
            minSum = min(num, tmp, minSum * num)
            res = max(res, maxSum, minSum)

        return res

nums = [2,3,-2,4]

print(maxProduct(nums))