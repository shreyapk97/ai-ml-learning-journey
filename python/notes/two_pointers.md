# Two Pointers

When to Use:
- Sorted arrays
- Pair sum problems

Template:

left = 0
right = len(nums) - 1

while left < right:

    current = nums[left] + nums[right]

    if current == target:
        return True

    elif current < target:
        left += 1

    else:
        right -= 1

Time:
O(n)

Space:
O(1)

Example:

nums = [1,2,3,4,5,6,7]
target = 9

Pairs:
(2,7)
(3,6)
(4,5)
