from collections import Counter, defaultdict


def find_duplicate_values(numbers):
    """Return the distinct values that appear more than once."""
    return {number for number, count in Counter(numbers).items() if count > 1}


def filter_long_vowel_words(words):
    """Keep words longer than four letters that start with a vowel."""
    return [word for word in words if len(word) > 4 and word[0].lower() in "aeiou"]


def group_anagrams(words):
    """Group words by their sorted-letter signature."""
    groups = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)
    return dict(groups)