import sys
from typing import List


def get_max_product_of_pairs(list_a: List[int],
                             list_b: List[int]) -> int:
    """
    get the max dot product of two lists under
    some permutation
    """

    list_a.sort(reverse=True)
    list_b.sort(reverse=True)
    total = sum([a * b for a, b in zip(list_a, list_b)])
    return total


if __name__ == "__main__":

    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
