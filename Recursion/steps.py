"""Problem: Count the number of ways to climb a staircase of n steps, where you can either take 1 or 2 steps at a time.
Example:
Input: 4
Output: 5"""

def steps(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    
    return steps(n - 1) + steps(n - 2)

print(steps(4))