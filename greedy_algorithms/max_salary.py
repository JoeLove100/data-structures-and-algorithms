import functools
import sys
from typing import List


def _concat_compare(a: str,
                    b: str) -> int:
    """
    checks if a "is less than" b, where here we
    mean "will give a smaller figure when concatenated
    with other integers"
    """

    a_first = int(a + b)
    b_first = int(b + a)

    if a_first > b_first:
        return -1
    elif a_first < b_first:
        return 1
    else:
        return 0


def get_max_salary(figures: List[int]) -> int:
    """
    find max figure possible by concatenating the
    given integers
    """

    figures = list(map(str, figures))
    figures.sort(key=functools.cmp_to_key(_concat_compare))
    max_salary = int("".join(figures))
    return max_salary


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = input_data.split()
    a = data[1:]
    print(get_max_salary(a))
