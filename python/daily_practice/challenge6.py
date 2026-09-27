from collections import Counter, defaultdict


def find_duplicates(numbers):
    """Return distinct values that appear more than once."""
    return {number for number, count in Counter(numbers).items() if count > 1}


def group_words_by_length(words):
    """Group words into lists keyed by their length."""
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)


def find_consecutive_runs(numbers):
    """Return sorted runs of adjacent integers found in the input."""
    unique_numbers = sorted(set(numbers))
    runs = []
    current_run = []
    for number in unique_numbers:
        if current_run and number != current_run[-1] + 1:
            if len(current_run) > 1:
                runs.append(current_run)
            current_run = []
        current_run.append(number)
    if len(current_run) > 1:
        runs.append(current_run)
    return runs