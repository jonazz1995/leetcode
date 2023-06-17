
def countPartitions(n,m):
    if n == 0: return 1
    if m == 0 or n < 0: return 0

    return countPartitions(n - m, m) + countPartitions(n, m - 1)

print(countPartitions(9,5))

