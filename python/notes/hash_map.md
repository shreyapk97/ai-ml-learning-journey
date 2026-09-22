# Hash Map Pattern

Use when:
- Need fast lookup
- Need counting/frequency
- Need to remember previously seen elements

Time Complexity:
- Lookup: O(1)
- Insert: O(1)

Common Problems:
- Two Sum
- Anagrams
- Frequency counting
- First unique element

Template:

freq = {}

for item in items:
    freq[item] = freq.get(item, 0) + 1
