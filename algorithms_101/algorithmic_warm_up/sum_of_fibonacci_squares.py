"""
The fibonacci numbers are period mod 10, hence so
are their squares, hence so is the cumulative
sum
"""

from algorithms_101.algorithmic_warm_up.fibonacci_numbers import fib_number_generator


def get_last_digit_of_fib_sum_squares(n: int) -> int:
    """
    return the last digit of the sum of the squares of
    the fibonacci numbers up to n
    """

    # TODO: would be interesting to see if this could be made to work
    # TODO: for arbitrary modulo k by working out the periodicity

    cycle_length = 30
    g = fib_number_generator()
    fib_number_squares = [next(g) ** 2 % 10 for _ in range(cycle_length)]
    fib_number_squares_sums = [sum(fib_number_squares[:i]) % 10 for i in range(1, cycle_length + 1)]

    last_digit = fib_number_squares_sums[n % cycle_length]
    return last_digit


if __name__ == "__main__":

    number = int(input())
    print(get_last_digit_of_fib_sum_squares(number))

