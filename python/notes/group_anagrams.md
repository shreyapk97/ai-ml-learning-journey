# Group Anagrams

Example:

["listen", "silent", "enlist"]

Key idea:

sorted("listen")
-> "eilnst"

All anagrams produce same sorted string.

Approach:

groups = {}

for word in words:
    key = ''.join(sorted(word))
    groups.setdefault(key, []).append(word)

Time:
O(n * k log k)

where:
n = number of words
k = average word length
