import sys
import math
from typing import List


def _binary_search(arr: List[int],
                   key: int,
                   l: int,
                   h: int) -> int:
    """
    get the position of x in A if it lies
    between h and l, returning -1 if it
    cannot be found
    """

    if l > h:
        # empty array, x not found
        return -1

    mid = math.floor(l + (h - l) / 2)

    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return _binary_search(arr, key, mid + 1, h)
    else:
        return _binary_search(arr, key, l, mid - 1)


def binary_search(arr: List[int],
                  key: int) -> int:
    """
    wrapper for the _binary_search function
    which defines the higher and lower bounds
    """

    return _binary_search(arr, key, 0, len(arr) - 1)


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')
