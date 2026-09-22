# Missing Number

Question:

[1,2,3,5]

Answer:
4

Approach 1: Set

num_set = set(nums)

for i in range(min(nums), max(nums)):
    if i not in num_set:
        print(i)

Time:
O(n)

Approach 2: Sum Formula

Expected:
n(n+1)/2

Missing =
Expected - Actual

Useful when numbers are consecutive.
