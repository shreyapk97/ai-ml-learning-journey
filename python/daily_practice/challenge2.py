from collections import Counter, defaultdict


def find_duplicates(numbers):
    """Return values that occur more than once, in first-seen order."""
    return [number for number, count in Counter(numbers).items() if count > 1]


def square_even_numbers(numbers):
    """Return the squares of the even numbers in the input."""
    return [number ** 2 for number in numbers if number % 2 == 0]


def group_anagrams_manual(words):
    """Group words with matching sorted-letter signatures."""
    signatures = {}
    for word in words:
        signatures.setdefault(tuple(sorted(word)), []).append(word)
    return list(signatures.values())


def group_anagrams(words):
    """Group anagrams using a default dictionary of word lists."""
    groups = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)
    return dict(groups)