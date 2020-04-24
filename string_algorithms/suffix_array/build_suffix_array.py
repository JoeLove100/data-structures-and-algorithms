from collections import defaultdict


def get_sorted_text(text: str):
    """
    sort the text by using counting sort and
    return list of sorted positions
    """

    positions = [0 for _ in range(len(text))]
    count = defaultdict(lambda: 0)

    for letter in text:
        count[letter] += 1

    all_letters = sorted(count)
    for i, letter in enumerate(all_letters[1:]):
        count[letter] += count[all_letters[i]]

    for i in list(range(len(text)))[::-1]:
        letter = text[i]
        positions[count[letter] - 1] = i
        count[letter] -= 1

    return positions


def get_character_classes(text: str):

    classes = defaultdict(lambda: 0)

    counter = 0
    for letter in sorted(list(set(text))):
        classes[letter] += counter
        counter += 1

    output = [0 for _ in range(len(text))]
    for i, letter in enumerate(text):
        output[i] = classes[letter]

    return output


def get_order_doubled(text: str,
                      cycle_length: int,
                      orders,
                      classes):
    """
    get sorted order of cyclic rotations of
    length 2 * cycle_length
    """

    count = [0 for _ in range(len(text))]
    new_order = [0 for _ in range(len(text))]

    for i in range(len(count)):
        count[classes[i]] += 1

    for j in range(1, len(count)):
        count[j] += count[j - 1]

    for k in range(len(text) - 1, -1, -1):
        start = (orders[k] - cycle_length + len(text)) % len(text)
        start_class = classes[start]
        count[start_class] -= 1
        new_order[count[start_class]] = start

    return new_order


def get_updated_classes(cycle_length: int,
                        orders,
                        classes):

    new_classes = [0 for _ in range(len(classes))]
    new_classes[orders[0]] = 0

    for i in range(1, len(orders)):
        current = orders[i]
        prev = orders[i - 1]
        mid = (current + cycle_length) % len(new_classes)
        mid_prev = (prev + cycle_length) % len(new_classes)
        if classes[current] == classes[prev] and classes[mid] == classes[mid_prev]:
            new_classes[current] = new_classes[prev]
        else:
            new_classes[current] = new_classes[prev] + 1

    return new_classes


def get_ordered_suffixes(text: str):

    orders = get_sorted_text(text)
    classes = get_character_classes(text)
    length = 1

    while length <= len(text):

        orders = get_order_doubled(text, length, orders, classes)
        classes = get_updated_classes(length, orders, classes)
        length *= 2

    return orders


if __name__ == "__main__":

    input_text = input().strip()
    ordered_suffixes = get_ordered_suffixes(input_text)
    for n in ordered_suffixes:
        print(n, end=" ")
