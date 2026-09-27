from collections import Counter, defaultdict


def unique_preserving_order(numbers):
    """Return the input values once each, preserving their original order."""
    return list(dict.fromkeys(numbers))


def intersection(first, second):
    """Return the distinct values shared by both iterables."""
    return list(set(first).intersection(second))


def even_squares(limit):
    """Return squares of even integers from zero through the given limit."""
    return [number ** 2 for number in range(limit + 1) if number % 2 == 0]


def group_anagrams(words):
    """Group anagrams and return the groups as a dictionary."""
    groups = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)
    return dict(groups)


def are_anagrams(first, second):
    """Check whether two strings contain the same characters."""
    return sorted(first) == sorted(second)


def sort_by_frequency(numbers):
    """Return a frequency dictionary ordered from most to least frequent."""
    counts = Counter(numbers)
    return dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))