import sys
from typing import List


def get_pisanto_period_sequence(m: int) -> List[int]:
    """
    get a sequence of numbers which represents the
    the repeating cycle of numbers produced by taking
    the fibonacci numbers module m
    """

    sequence = [0, 1]

    while len(sequence) <= 2 or sequence[-2:] != [0, 1]:
        sequence.append((sequence[-1] + sequence[-2]) % m)

    return sequence[:-2]  # [:-2] as we don't want to return the repeated 0, 1


def get_nth_fib_modulo_m(n: int,
                         m: int) -> int:
    """
    get the nth fibonacci number modulo m
    """

    repeating_sequence = get_pisanto_period_sequence(m)
    fib_number = repeating_sequence[n % len(repeating_sequence)]
    return fib_number


if __name__ == "__main__":

    input_data = sys.stdin.read()
    n_1, n_2 = map(int, input_data.split())
    print(get_nth_fib_modulo_m(n_1, n_2))

