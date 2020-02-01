from typing import Generator, Any


def fib_number_generator() -> Generator[int, None, None]:
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


def get_nth_generator_value(n: int,
                            g: Generator) -> Any:
    """
    return the nth value from a generator
    """

    nth_value = next(x for i, x in enumerate(g) if i == n)
    return nth_value


def get_nth_fib_number(n):
    """
    get the nth fibonacci number using
    a more efficient iterative method
    """

    g = fib_number_generator()
    fib_number = get_nth_generator_value(n, g)
    return fib_number


if __name__ == "__main__":
    number = int(input())
    print(get_nth_fib_number(number))
