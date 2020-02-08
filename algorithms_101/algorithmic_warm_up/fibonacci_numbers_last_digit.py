from typing import Generator
from algorithms_101.algorithmic_warm_up.fibonacci_numbers import get_nth_generator_value


def _fib_last_digit_generator() -> Generator:
    """
    generator for the last digit of the
    fibonacci numbers
    """

    yield 0
    yield 1

    n_2 = 0
    n_1 = 1

    while True:

        n = (n_2 + n_1) % 10
        yield n

        n_2 = n_1
        n_1 = n


def last_digit_of_fib(n: int) -> int:
    """
    get the last digit of the nth fibonacci
    number
    """

    g = _fib_last_digit_generator()
    last_digit = get_nth_generator_value(n, g)
    return last_digit


if __name__ == "__main__":

    number = int(input())
    print(last_digit_of_fib(number))


