import sys
from typing import List


def get_max_substring_length(list_a: List[int],
                             list_b: List[int]) -> int:
    """
    get the length of the largest common sub-sequence
    between list_a and list_b
    """

    width = len(list_a) + 1
    length = len(list_b) + 1
    arr = [[0 for _ in range(width)] for _ in range(length)]

    for i in range(1, width):
        for j in range(1, length):

            insertion = arr[j - 1][i]
            deletion = arr[j][i - 1]
            swap = arr[j - 1][i - 1]

            if list_a[i - 1] == list_b[j - 1]:
                swap += 1

            arr[j][i] = max(insertion, deletion, swap)

    return arr[-1][-1]


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(get_max_substring_length(a, b))
