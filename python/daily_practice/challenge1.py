from collections import Counter


def count_vowels(text):
    """Count lowercase vowels in a string."""
    character_counts = Counter(text)
    return sum(character_counts[vowel] for vowel in "aeiou")


def count_words(sentence):
    """Return a frequency dictionary for the words in a sentence."""
    frequencies = {}
    for word in sentence.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def two_sum(numbers, target):
    """Return index pairs whose values add up to the target."""
    pairs = []
    for first_index, number in enumerate(numbers):
        for second_index in range(first_index + 1, len(numbers)):
            if number + numbers[second_index] == target:
                pairs.append((first_index, second_index))
    return pairs
            
