def bottom_up_fib(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]

print('Bottom up fib: ')
print(bottom_up_fib(6))

def top_down_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return top_down_fib(n-1) + top_down_fib(n-2)

print('Top up fib: ')
print(top_down_fib(6))