'''Problem: Calculate the factorial of a number recursively.
    Example:
    Input: 5
    Output: 120'''

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

# print(factorial(100))

'''Problem: Generate all possible permutations of a string recursively.
Example:
Input: "abc"
Output: ["abc", "acb", "bac", "bca", "cab", "cba"]'''

def permutations(str):
    pass