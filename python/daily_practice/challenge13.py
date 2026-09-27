from collections import Counter


def longest_consecutive_length(numbers):
    """Return the length of the longest consecutive integer sequence."""
    number_set = set(numbers)
    longest = 0
    for number in number_set:
        if number - 1 not in number_set:
            end = number
            while end + 1 in number_set:
                end += 1
            longest = max(longest, end - number + 1)
    return longest


def top_k_frequent(numbers, k):
    """Return the k most frequent values, preserving first-seen tie order."""
    return [number for number, _ in Counter(numbers).most_common(k)]


def encode_words(words):
    """Prefix each word with its character count and concatenate the results."""
    return "".join(f"{len(word)}{word}" for word in words)




