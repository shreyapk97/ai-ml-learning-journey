from collections import Counter, deque


def second_largest_unique(numbers):
    """Return the second-largest distinct number, or None if unavailable."""
    unique_numbers = sorted(set(numbers), reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None


def rotate_right(numbers, steps):
    """Return a copy of the list rotated right by the given number of steps."""
    rotated = deque(numbers)
    rotated.rotate(steps)
    return list(rotated)


def longest_distinct_permutation_length(text):
    """Return the greatest possible length of a permutation without repeats."""
    return len(set(text))


def first_nonrepeating_character(text):
    """Return the first character that occurs exactly once, or None."""
    counts = Counter(text)
    return next((character for character in text if counts[character] == 1), None)


def two_sum_indices(numbers, target):
    """Return indices of one pair of values whose sum equals the target."""
    seen_indices = {}
    for index, number in enumerate(numbers):
        complement = target - number
        if complement in seen_indices:
            return seen_indices[complement], index
        seen_indices[number] = index
    return None



