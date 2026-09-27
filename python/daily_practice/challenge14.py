from collections import Counter


def find_missing_numbers(numbers):
    """Return missing integers strictly between the smallest and largest values."""
    if not numbers:
        return []
    number_set = set(numbers)
    return [number for number in range(min(number_set), max(number_set) + 1)
            if number not in number_set]


def top_k_frequent(numbers, k):
    """Return the k most frequent values, preserving first-seen tie order."""
    return [number for number, _ in Counter(numbers).most_common(k)]


def is_valid_sudoku(board):
    """Check a 9-by-9 Sudoku board for row, column, and box duplicates."""
    if len(board) != 9 or any(len(row) != 9 for row in board):
        return False
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for row_index, row in enumerate(board):
        for column_index, value in enumerate(row):
            if value in (0, "0", "."):
                continue
            if str(value) not in "123456789":
                return False
            box_index = (row_index // 3) * 3 + column_index // 3
            if (value in rows[row_index] or value in columns[column_index]
                    or value in boxes[box_index]):
                return False
            rows[row_index].add(value)
            columns[column_index].add(value)
            boxes[box_index].add(value)
    return True
        