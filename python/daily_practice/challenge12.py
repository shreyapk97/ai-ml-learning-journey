from collections import Counter, defaultdict


def get_longest_subseq_length(numbers):
    """Return the length of the longest sequence of consecutive integers."""
    number_set = set(numbers)
    longest = 0
    for number in number_set:
        if number - 1 not in number_set:
            end = number
            while end + 1 in number_set:
                end += 1
            longest = max(longest, end - number + 1)
    return longest


def group_similar_strings(words):
    """Group words whose letters follow the same cyclic shift pattern."""
    groups = defaultdict(list)
    for word in words:
        if word:
            signature = tuple(
                (ord(word[index]) - ord(word[index - 1])) % 26
                for index in range(len(word))
            )
        else:
            signature = ()
        groups[signature].append(word)
    return list(groups.values())


def first_nonrepeating_character(text):
    """Return the first character that occurs once, or None if all repeat."""
    counts = Counter(text)
    return next((character for character in text if counts[character] == 1), None)


