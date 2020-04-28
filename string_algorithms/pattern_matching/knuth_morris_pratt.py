from typing import List


def get_all_prefixes(text: str) -> List[int]:

    all_borders = [0]
    current_border = 0

    for i in range(1, len(text)):

        while current_border > 0 and text[i] != text[current_border]:
            current_border = all_borders[current_border - 1]

        if text[i] == text[current_border]:
            current_border += 1

        all_borders.append(current_border)

    return all_borders


def get_pattern_occurrences(text: str,
                            pattern: str) -> List[int]:

    if len(pattern) > len(text):
        return []

    new_text = "".join([pattern, "$", text])
    prefixes = get_all_prefixes(new_text)
    positions = []

    for i in range(len(pattern), len(new_text)):
        if prefixes[i] == len(pattern):
            positions.append(i - 2 * len(pattern))

    return positions


if __name__ == "__main__":

    input_pattern = input().strip()
    input_text = input().strip()

    positions = get_pattern_occurrences(input_text, input_pattern)
    for p in positions:
        print(p, end=" ")
