import sys
import math
from typing import List


def _merge(arr: List[int],
           low: int,
           m: int,
           high: int) -> int:
    """
    merge the two sorted arrays arr[low: m]
    and arr[m: high] and return the number
    of inversions involved in doing so
    """

    i = low
    j = m
    inv = 0
    merged_arr = [None] * (high - low)

    for k in range(len(merged_arr)):
        if arr[i] <= arr[j]:
            merged_arr[k] = arr[i]
            i += 1
            if i >= m:
                merged_arr[k + 1:] = arr[j:high]
                break
        else:
            merged_arr[k] = arr[j]
            j += 1
            inv += len(arr[i:m])

            if j >= high:
                merged_arr[k + 1:] = arr[i: m]
                break

    arr[low: high] = merged_arr

    return inv


def _merge_sort(arr: List[int],
                low: int,
                high: int) -> int:
    """
    use a merge sort procedure to sort the array
    between high and low, and return the number
    of inversions in doing so
    """

    if low >= high - 1:
        return 0

    inv = 0
    m = math.floor(low + (high - low) / 2)
    inv += _merge_sort(arr, low, m)
    inv += _merge_sort(arr, m, high)

    return inv + _merge(arr, low, m, high)


def merge_sort(arr: List[int]) -> int:
    """
    sort the array by merge sort and return
    the number of inversions involved in
    doing so
    """

    return _merge_sort(arr, 0, len(arr))


if __name__ == '__main__':
    input_data = sys.stdin.read()
    n, *a = list(map(int, input_data.split()))
    b = n * [0]
    print(merge_sort(a))
