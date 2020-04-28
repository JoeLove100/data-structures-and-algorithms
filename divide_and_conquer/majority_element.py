import sys
from typing import List, Tuple


def _get_element_orders(arr: List[int],
                        key: int) -> Tuple[List[int], List[int], int]:
    """
    return two lists - one of figures less than
    key and one of those greater - and the count
    of key in arr
    """

    less, greater, equal = [], [], 0

    for i in arr:
        if i < key:
            less.append(i)
        elif i > key:
            greater.append(i)
        else:
            equal += 1

    return less, greater, equal


def _get_majority_element(arr: List[int],
                          majority_size: int) -> int:
    """
    return the value of the majority element between
    l and h if this element exists, and return
    -1 if no such element exists
    """

    less_than, greater_than, equal = _get_element_orders(arr, arr[0])

    if equal > majority_size:
        return arr[0]
    elif len(less_than) > majority_size:
        return _get_majority_element(less_than, majority_size)
    elif len(greater_than) > majority_size:
        return _get_majority_element(greater_than, majority_size)
    else:
        return -1


def get_majority_element(arr: List[int]) -> int:
    """
    wrapper function for _get_majority_element which
    calculates the majority size
    """

    majority_size = len(arr) / 2
    return _get_majority_element(arr, majority_size)


if __name__ == '__main__':
    input_data = sys.stdin.read()
    n, *a = list(map(int, input_data.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
