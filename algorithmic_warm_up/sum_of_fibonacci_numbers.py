"""
The below solution works on the observation that
the sum of the first n fibonacci numbers is equal
to the value of the n+2th numbers less 1
"""

import sys
from algorithmic_warm_up.pisanto_periods import get_nth_fib_modulo_m


def get_nth_fib_sum_modulon_m(n: int,
                              m: int) -> int:
    """
    get the value of the sum of the first n
    fibonacci numbers modulo m
    """

    # get the n+2 th value
    val = get_nth_fib_modulo_m(n + 2, m)

    # handle the -1 for the modular arithmetic
    if val == 0:
        return m - 1
    else:
        return val - 1


if __name__ == "__main__":

    number = int(input())
    print(get_nth_fib_sum_modulon_m(number, 10))

