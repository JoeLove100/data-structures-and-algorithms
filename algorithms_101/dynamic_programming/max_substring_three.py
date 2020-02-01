import sys
from typing import List


def get_max_sub_sequence_length(list_a: List[int],
                                list_b: List[int],
                                list_c: List[int]) -> int:
    """
    get the length max sub-sequence of the three in put
    lists
    """

    width = len(list_a) + 1
    length = len(list_b) + 1
    height = len(list_c) + 1
    arr = [[[0 for _ in range(width)] for _ in range(length)] for _ in range(height)]

    for i in range(1, width):
        for j in range(1, length):
            for k in range(1, height):

                change_1 = arr[k - 1][j][i]
                change_2 = arr[k][j - 1][i]
                change_3 = arr[k][j][i - 1]
                change_4 = arr[k - 1][j - 1][i]
                change_5 = arr[k - 1][j][i - 1]
                change_6 = arr[k][j - 1][i - 1]
                change_7 = arr[k - 1][j - 1][i - 1]

                if list_a[i - 1] == list_b[j - 1] == list_c[k - 1]:
                    change_7 += 1

                arr[k][j][i] = max([change_1, change_2, change_3, change_4, change_5, change_6, change_7])

    return arr[-1][-1][-1]


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(get_max_sub_sequence_length(a, b, c))
