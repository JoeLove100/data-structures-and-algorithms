import math
from typing import List, Tuple


def _parent(i: int) -> int:
    """
    get the parent index of i
    """

    return math.floor(i / 2)


def _left_child(i: int) -> int:
    """
    get the left child index of i
    """

    return 2 * i


def _right_child(i: int) -> int:
    """
    get the right child index of i
    """

    return 2 * i + 1


def _shift_down(i: int,
                data: List[int],
                swaps: List[Tuple[int, int]]) -> None:
    """
    shift the element i down to its correct
    position
    """

    left_ind = _left_child(i)
    left_val = data[left_ind - 1] if left_ind <= len(data) else math.inf
    right_ind = _right_child(i)
    right_val = data[right_ind - 1] if right_ind <= len(data) else math.inf

    if left_val < right_val and data[i - 1] > left_val:
        # left child is smaller, swap with left child
        data[i - 1], data[left_ind - 1] = data[left_ind - 1], data[i - 1]
        swaps.append((i - 1, left_ind - 1))
        _shift_down(left_ind, data, swaps)
    elif right_val <= left_val and data[i - 1] > right_val:
        # right child is smaller, swap with right child
        data[i - 1], data[right_ind - 1] = data[right_ind - 1], data[i - 1]
        swaps.append((i - 1, right_ind - 1))
        _shift_down(right_ind, data, swaps)
    else:
        # both larger than data[i - 1], so ignore
        pass


def build_heap(data: List[int]) -> List[Tuple[int, int]]:
    """
    convert the input data to a min-heap structure
    and return a list of the required swaps
    """

    swaps = []

    for i in range(math.floor((len(data) + 1) / 2), 0, -1):
        _shift_down(i, data, swaps)

    return swaps


def build_heap_slow(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
