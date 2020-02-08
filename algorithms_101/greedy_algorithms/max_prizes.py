import sys
from typing import List


def optimal_summands(n: int) -> List[int]:
    """
    for a given n, get a set of optimal prize
    values so that all are pairwise distinct and we
    have as many as possible
    """

    optimal_vals = []
    val = 1
    remaining_n = n

    while True:

        if remaining_n < 2 * val + 1:
            optimal_vals.append(remaining_n)
            break
        else:
            optimal_vals.append(val)
            remaining_n -= val
            val += 1

    return optimal_vals


if __name__ == "__main__":

    input = sys.stdin.read()
    number = int(input)
    summands = optimal_summands(number)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
