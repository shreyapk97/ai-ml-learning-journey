# First Non-Repeating Element

Question:
Find first character or number appearing exactly once.

Approach:

from collections import Counter

freq = Counter(items)

for item in items:
    if freq[item] == 1:
        print(item)
        break

Time:
O(n)

Why it works:
Counter gives frequency.
Second pass preserves original order.
