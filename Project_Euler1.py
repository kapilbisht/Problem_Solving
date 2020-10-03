# Multiples of 3 and 5
# Problem ---
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below N.
# Input Format --
# First line contains T that denotes the number of test cases.
# This is followed by T lines, each containing an integer, N.
# Constraints
# 1 <= T <= 10 ^ 5
# 1 <= N <= 10 ^ 9

# Solution
def sum(n, k):
    d = n // k
    return k * (d * (d + 1)) // 2


def eulerDef(n):
    return sum(n, 3) + sum(n, 5) - sum(n, 15)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(eulerDef(n - 1))  # Below N
