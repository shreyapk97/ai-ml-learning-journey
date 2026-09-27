from collections import Counter, defaultdict


def first_unique_number(numbers):
    """Return the first number that occurs once, or None if none exists."""
    counts = Counter(numbers)
    return next((number for number in numbers if counts[number] == 1), None)


def group_anagrams(words):
    """Group words by their sorted-letter signature."""
    groups = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)
    return dict(groups)


def product_except_self(numbers):
    """Return products of all values except the value at each position."""
    products = []
    for index in range(len(numbers)):
        product = 1
        for other_index, number in enumerate(numbers):
            if other_index != index:
                product *= number
        products.append(product)
    return products


def two_sum_sorted(numbers, target):
    """Find value pairs in a sorted list that add up to the target."""
    left, right = 0, len(numbers) - 1
    pairs = []
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            pairs.append((numbers[left], numbers[right]))
            left += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1
    return pairs


def product_except_self_prefix_suffix(numbers):
    """Compute each excluded product using running prefix and suffix products."""
    products = [1] * len(numbers)
    prefix_product = 1
    for index, number in enumerate(numbers):
        products[index] = prefix_product
        prefix_product *= number
    suffix_product = 1
    for index in range(len(numbers) - 1, -1, -1):
        products[index] *= suffix_product
        suffix_product *= numbers[index]
    return products
