from collections import defaultdict


def find_missing_successors(numbers):
    """Find absent next integers between present values and the maximum."""
    number_set = set(numbers)
    return [number + 1 for number in number_set if number + 1 not in number_set
            and number + 1 < max(number_set)] if number_set else []


def group_words_by_length(words):
    """Group words into lists keyed by their length."""
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)


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


def find_two_sum_pairs(numbers, target):
    """Return distinct value pairs that sum to the target."""
    pairs = set()
    number_set = set(numbers)
    for number in number_set:
        complement = target - number
        if complement in number_set:
            pairs.add(tuple(sorted((number, complement))))
    return pairs