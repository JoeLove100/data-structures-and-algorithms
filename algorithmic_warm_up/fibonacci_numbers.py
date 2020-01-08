from typing import Generator


def _fib_number_generator() -> Generator[int, None, None]:
    """
    generator for fibonacci numbers
    """

    yield 0
    yield 1

    n_1 = 1
    n_2 = 0

    while True:

        # add two previous numbers to get fib number
        n = n_1 + n_2
        yield n

        # move forward to next pair of numbers
        n_2 = n_1
        n_1 = n


def get_nth_fib_number(n: int) -> int:
    """
    get the nth fibonacci number using
    a faster iterative method
    """

    if n <= 1:
        return n
    else:
        fib_generator = _fib_number_generator()

        for _ in range(n):
            next(fib_generator)

        return next(fib_generator)


def calc_fib_slow(n: int) -> int:
    """
    get the nth fibonacci number using a
    recursive method with exponential time
    complexity
    """

    if n <= 1:
        return n

    return calc_fib_slow(n - 1) + calc_fib_slow(n - 2)


if __name__ == "__main__":
    number = int(input())
    print(get_nth_fib_number(number))
