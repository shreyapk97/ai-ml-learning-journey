from collections import Counter


def compress_character_counts(text):
    """Encode each distinct character with its total frequency."""
    counts = Counter(text)
    return "".join(
        character if count == 1 else character + str(count)
        for character, count in counts.items()
    )


def longest_consecutive_length(numbers):
    """Return the length of the longest run of consecutive integers."""
    number_set = set(numbers)
    longest = 0
    for number in number_set:
        if number - 1 not in number_set:
            current = number
            length = 1
            while current + 1 in number_set:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest
    if nums_sorted[i]-1 in nums_sorted:

        count+=1

        i+=1
