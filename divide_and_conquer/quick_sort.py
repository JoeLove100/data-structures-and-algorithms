import sys
from random import Random
from typing import List, Tuple


def _partition_three(arr: List[int],
                     low: int,
                     high: int) -> Tuple[int, int]:
    """
    sort the array into three sections (greater than,
    equal to, less than the pivot) and return the
    first and last index of elements equal to the
    pivot
   """

    pivot = arr[low]
    j = low
    k = low

    for i in range(low + 1, high + 1):
        if arr[i] < pivot:
            j += 1
            k += 1
            arr[k], arr[i] = arr[i], arr[k]
            arr[k], arr[j] = arr[j], arr[k]
        elif arr[i] == pivot:
            k += 1
            arr[k], arr[i] = arr[i], arr[k]

    arr[j], arr[low] = arr[low], arr[j]

    return j, k


def _partition2(arr: List[int],
                low: int,
                high: int) -> int:
    """
    sort the array so the pivot is in
    the correct position, and then return
    the index of the pivot
    """

    pivot = arr[low]
    j = low
    for i in range(low + 1, high + 1):
        if arr[i] <= pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


def _randomized_quick_sort(arr: List[int],
                           low: int,
                           high: int,
                           rnd: Random) -> None:
    """
    sort the array using a three-way quick
    sort algorithm
    """

    if low >= high:
        return

    # swap to get random pivot
    rand_piv = rnd.randint(low, high)
    arr[low], arr[rand_piv] = arr[rand_piv], arr[low]

    # get the partition
    j, k = _partition_three(arr, low, high)

    # recursive sort of series above/below
    _randomized_quick_sort(arr, low, j - 1, rnd)
    _randomized_quick_sort(arr, k + 1, high, rnd)


def randomized_quick_sort(arr: List[int],
                          rnd: Random) -> None:
    """
    wrapper for _randomized_quick_sort which handles
    the initial high and low
    """

    _randomized_quick_sort(arr, 0, len(arr) - 1, rnd)


if __name__ == '__main__':
    input_data = sys.stdin.read()
    n, *a = list(map(int, input_data.split()))
    randomizer = Random()
    _randomized_quick_sort(a, 0, n - 1, randomizer)
    for x in a:
        print(x, end=' ')
