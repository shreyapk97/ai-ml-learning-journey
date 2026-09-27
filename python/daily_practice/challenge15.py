from collections import Counter


def find_peak(numbers):
    """Return the largest value in the input, or None when it is empty."""
    return max(numbers) if numbers else None


def top_k_frequent(numbers, k):
    """Return the k most frequent values, preserving first-seen tie order."""
    return [number for number, _ in Counter(numbers).most_common(k)]


def spiral_traversal(matrix):
    """Return matrix values in clockwise spiral order."""
    if not matrix or not matrix[0]:
        return []
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        result.extend(matrix[top][left:right + 1])
        top += 1
        for row_index in range(top, bottom + 1):
            result.append(matrix[row_index][right])
        right -= 1
        if top <= bottom:
            result.extend(reversed(matrix[bottom][left:right + 1]))
            bottom -= 1
        if left <= right:
            for row_index in range(bottom, top - 1, -1):
                result.append(matrix[row_index][left])
            left += 1
    return result