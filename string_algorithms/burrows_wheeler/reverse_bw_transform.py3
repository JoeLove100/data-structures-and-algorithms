from collections import Counter


def get_start_positions(text: str):
    """
    get a dictionary giving the starting
    position of each unique letter in text in
    the sorted version of text
    """

    unique = sorted(list(set(text)))
    item_counts = Counter(text)
    initial_positions = dict()
    prev_item_count = 0

    for l in unique:
        initial_positions[l] = prev_item_count
        prev_item_count += item_counts[l]

    return initial_positions


def build_first_last_mapping(text: str):
    """
    build a first-last mapping for the
    Burrows-Wheeler inverse transform
    """

    item_positions = get_start_positions(text)

    first_last_mapping = dict()
    for idx, letter in enumerate(text):
        position_in_sorted = item_positions[letter]
        first_last_mapping.update({idx: position_in_sorted})
        item_positions[letter] += 1

    return first_last_mapping


def reverse_bw_transform(text: str) -> str:
    """
    reverse BW transform of text using 
    the first-last algorithm    
    """

    first_last_mapping = build_first_last_mapping(text)
    pos = 0
    output_string = ["$"]

    while True:
        next_pos = first_last_mapping.get(pos)
        if next_pos == 0:
            break
        else:
            output_string.append(text[pos])
            first_last_mapping.pop(pos)
            pos = next_pos

    return "".join(reversed(output_string))


if __name__ == "__main__":

    txt = input().strip()
    print(reverse_bw_transform(txt))


