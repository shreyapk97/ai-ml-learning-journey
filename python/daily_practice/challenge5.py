from collections import Counter, defaultdict


def find_duplicates(numbers):
    """Return unique values that occur at least twice."""
    return {number for number, count in Counter(numbers).items() if count > 1}


def group_words_by_length(words):
    """Group words into lists keyed by their length."""
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)


def group_anagrams(words):
    """Group words that are anagrams of one another."""
    groups = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)
    return dict(groups)