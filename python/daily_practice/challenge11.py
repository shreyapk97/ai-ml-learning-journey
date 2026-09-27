from collections import Counter


def get_most_freq_word(words):
    """Return the most frequent word, choosing its earliest occurrence on ties."""
    if not words:
        return None
    counts = Counter(words)
    return max(dict.fromkeys(words), key=counts.get)


def get_longest_nonrepeating_substring(text):
    """Return the length of the longest substring with no repeated characters."""
    last_seen = {}
    window_start = 0
    longest = 0
    for index, character in enumerate(text):
        if character in last_seen and last_seen[character] >= window_start:
            window_start = last_seen[character] + 1
        last_seen[character] = index
        longest = max(longest, index - window_start + 1)
    return longest


def get_valid_parentheses(text):
    """Check whether every opening bracket has a correctly matched closing bracket."""
    matching_openers = {")": "(", "]": "[", "}": "{"}
    stack = []
    for character in text:
        if character in "([{":
            stack.append(character)
        elif character in matching_openers:
            if not stack or stack.pop() != matching_openers[character]:
                return False
    return not stack


def first_nonrepeating_character(text):
    """Return the first character that occurs once, or None if all repeat."""
    counts = Counter(text)
    return next((character for character in text if counts[character] == 1), None)