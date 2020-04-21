from typing import List
from collections import defaultdict


def get_sorted_text(text: str) -> List[int]:
    """
    sort the text by using counting sort and
    return list of sorted positions
    """

    positions = [0 for _ in range(len(text))]
    count = defaultdict(lambda : 0)

    for letter in text:
        count[letter] += 1

    all_letters = sorted(count)
    for i, letter in enumerate(all_letters[1:]):
        count[letter] += count[all_letters[i]]

    for i in list(range(len(text)))[::-1]:
        letter = text[i]
        positions[i] = count[letter] - 1
        count[letter] -= 1

    return positions
